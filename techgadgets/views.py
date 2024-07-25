from locale import currency
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, JsonResponse, HttpResponseNotFound
import json
from django.utils.text import slugify
from django.urls import reverse
from django.views import View
from django.views.generic.base import RedirectView

from techgadgets.models import Gadget

from .dummy_data import gadgets

# Create your views here.


class RedirectToGadgetView(RedirectView):
    pattern_name = "single_gadget_slug_url"

    def get_redirect_url(self, *args, **kwargs):
        slug = slugify(gadgets[kwargs.get("gadget_id", 0)]["name"])
        new_kwargs = {"gadget_slug": slug}
        return super().get_redirect_url(*args, **new_kwargs)


class GadgetView(View):
    def get(self, request, gadget_slug):
        gadget_match = None

        for gadget in gadgets:
            print(slugify(gadget["name"]))
            if slugify(gadget["name"]) == gadget_slug:
                gadget_match = gadget

        if gadget_match:
            return JsonResponse(gadget_match)
        raise Http404("Not found, try again")

    def post(self, request):
        print(request)
        try:
            data = json.loads(request.body)
            
            new_gadget = Gadget(
                name=data['name'],
                category=data['category'],
                manufacturer=data['manufacturer'],
                price=data['price'],
                currency=data['currency'],
                description=data['description']
            )
            new_gadget.save()
            return JsonResponse({"Success": "Funktioniert"}, status=200)
        except:
            
            return JsonResponse({"error": "Zonk!"}, status=400)


def start_page_view(request):
    return HttpResponse("Hello World")


def single_gadget_int_view(request, gadget_id):
    if len(gadgets) > gadget_id:
        new_slug = slugify(gadgets[gadget_id]["name"])
        new_url = reverse("single_gadget_slug_url", args=[new_slug])
        return redirect(new_url)

    return HttpResponseNotFound("Not found, try again")

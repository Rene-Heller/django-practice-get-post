from django.urls import path
from .views import GadgetView, RedirectToGadgetView, start_page_view, \
    single_gadget_int_view \
    


urlpatterns = [
    path("", RedirectToGadgetView.as_view()),
    path("gadget/", GadgetView.as_view()),
    path("<int:gadget_id>", single_gadget_int_view),
    path("gadget/<slug:gadget_slug>", GadgetView.as_view(),
         name="single_gadget_slug_url")
]

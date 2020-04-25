from django.urls import path
from . import views
from  django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("about",views.about,name="AboutUs"),
    path("contect",views.contect,name="ContectUs"),
    path("tracker",views.tracker,name="TrackingStatus"),
    path("search",views.search,name="SearchBar"),
    path("product/<int:myid>",views.prodView,name="productView"),
    path("checkout",views.checkout,name="CheckOuts")

] + static( settings.MEDIA_URL , document_root=settings.MEDIA_ROOT )
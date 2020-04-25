from django.urls import path
from . import views
urlpatterns = [
    path("",views.bloghome,name="BlogHome"),
    path("index",views.index,name="BlogHome")
]
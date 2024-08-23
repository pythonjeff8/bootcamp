from django.urls import path
from .views import AboutView, index

urlpatterns = [
    path('', index, name='index'),
    #path("about/", about, name = "about"),
    path("about/", AboutView.as_view(), name = "about"),
    
    ]

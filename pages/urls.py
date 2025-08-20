from django.urls import path
from .views import HomePageView, VuelosIndexView, VuelosShowView

urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path('vuelos/', VuelosIndexView.as_view(), name='index'),
    path('vuelos/<str:id>', VuelosShowView.as_view(), name='show'),
]
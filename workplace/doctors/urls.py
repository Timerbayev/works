from django.urls import path
from django.views.decorators.cache import cache_page

from .views import DoctorsView, HomeView

urlpatterns = [
    path('', cache_page(60)(HomeView.as_view()), name="home"),
    path('doctors', DoctorsView.as_view(), name="path_doctors"),
]
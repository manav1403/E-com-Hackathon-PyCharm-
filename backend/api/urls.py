from django.urls import path
from . import views


urlpatterns = [
    path('store', views.Store.as_view(), name="store"),
]
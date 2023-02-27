from django.urls import path

from . import views

urlpatterns = [
    path("<pk>", views.ProductDetailApi.as_view()),
    path("", views.p_createView)
]
from django.urls import path
from app import views

urlpatterns = [
    path("product/list/", views.product_list),
    path("product/create/", views.product_create),
    path("product/update/<int:pk>/", views.product_update),
    path("product/delete/<int:pk>/", views.product_delete),
]

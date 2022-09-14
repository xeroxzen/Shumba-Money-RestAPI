from django.urls import path
from .views import CustomerList, CustomerDetail


urlpatterns = [
    path("<int:pk>", CustomerDetail().as_view(), name="customer_detail"),
    path("", CustomerList().as_view(), name="customer_list"),

]
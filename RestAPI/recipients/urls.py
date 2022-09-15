from django.urls import path
from .views import RecipientList, RecipientDetail

urlpatterns = [
    path("<int:pk>/", RecipientDetail.as_view(), name="recipient_detail"),
    path("", RecipientList.as_view(), name="recipient_list"),

]
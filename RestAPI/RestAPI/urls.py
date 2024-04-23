from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

API_BASE_URL = "api/v1/"  # Define the constant

schema_view = get_swagger_view(title='Restful API')

urlpatterns = [
    path("admin/", admin.site.urls),
    path(API_BASE_URL, include("users.urls")),  # Use the constant
    path(API_BASE_URL, include("recipients.urls")),
    path(API_BASE_URL, include("transactions.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('swagger/', schema_view),
    path("", schema_view),
]

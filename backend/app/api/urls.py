from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from api.views import test_email

router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('test-email/', test_email),
    path('api-auth/', include('rest_framework.urls')),
]

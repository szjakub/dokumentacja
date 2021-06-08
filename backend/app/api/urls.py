from django.urls import path, include
from rest_framework import routers

from api.views import test_email

router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('test-email/', test_email),
    path('api-auth/', include('rest_framework.urls')),
]

from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import (
    SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
)
from api import views

router = routers.DefaultRouter()
router.register(r'schools', views.SchoolViewSet, basename='school')
router.register(r'classes', views.ClassViewSet, basename='class')
router.register(r'students', views.StudentViewSet, basename='student')
router.register(r'students', views.StudentReadOnlyViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

from django.urls import path, include
from rest_framework import routers
from drf_spectacular.views import (
    SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
)
from api.viewsets import (
    SchoolViewSet, SchoolClassViewSet, StudentViewSet, ObtainCyprusAuthTokenView
)


router = routers.DefaultRouter()
router.register(r'schools', SchoolViewSet, basename='school')
router.register(r'classes', SchoolClassViewSet, basename='class')
router.register(r'students', StudentViewSet, basename='student')


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', ObtainCyprusAuthTokenView.as_view(), name='auth-token'),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

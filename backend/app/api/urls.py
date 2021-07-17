from django.urls import path, include
from rest_framework import routers
from drf_spectacular.views import (
    SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
)
from api.views import (
    auth_views, school_views, school_class_views, student_views
)


router = routers.DefaultRouter()
router.register(r'schools', school_views.SchoolViewSet, basename='school')
router.register(r'classes', school_class_views.SchoolClassViewSet, basename='class')
router.register(r'students', student_views.StudentViewSet, basename='student')


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', auth_views.ObtainCyprusAuthTokenView.as_view(), name='auth-token'),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

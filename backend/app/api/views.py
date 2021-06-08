from rest_framework import viewsets
from school import models as school_models
from api.serializers import (
    PrincipalSerializer
)


class PrincipalViewSet(viewsets.ModelViewSet):
    queryset = school_models.School.objects.all()
    serializer_class = PrincipalSerializer

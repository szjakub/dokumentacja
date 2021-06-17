from rest_framework import generics
from rest_framework.permissions import AllowAny

from api.serializers import (
    SchoolSerializer
)


class CreateSchool(generics.CreateAPIView):
    serializer_class = SchoolSerializer
    permission_classes = [AllowAny]



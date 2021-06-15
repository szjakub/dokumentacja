from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny

from school.tasks import send_user_email
from api.serializers import (
    SchoolSerializer
)


@api_view(['GET'])
def test_email(request):
    send_user_email.delay()
    return Response({'sie': 'ma'})


class CreateSchool(generics.CreateAPIView):
    serializer_class = SchoolSerializer
    permission_classes = [AllowAny]



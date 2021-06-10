from rest_framework.response import Response
from rest_framework.decorators import api_view

from school.tasks import send_user_email


@api_view(['GET'])
def test_email(request):
    send_user_email.delay()
    return Response({'sie': 'ma'})



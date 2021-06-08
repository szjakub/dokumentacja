from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import send_mail


@api_view(['GET'])
def test_email(request):
    send_mail(
        'Subject here',
        'Here is the message.',
        'jakubszkodny@pepisandbox.com',
        ['jakubszkodny@gmail.com'],
    )
    return Response({'sie': 'ma'})



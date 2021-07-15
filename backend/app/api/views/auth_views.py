from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiExample


class ObtainCyprusAuthTokenView(ObtainAuthToken):
    @extend_schema(
        examples=[
            OpenApiExample(
                'Auth token return value',
                value={
                    'token': 'string',
                    'role': 'string'
                },
                response_only=True,
                request_only=False,
            ),
        ],
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'role': user.get_role_display()
        })

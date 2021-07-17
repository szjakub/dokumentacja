from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_400_BAD_REQUEST
from drf_spectacular.utils import extend_schema
from api.serializers.school_serializers import SchoolRequestSerializer


class SchoolViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    @extend_schema(
        request=SchoolRequestSerializer,
        responses={201: SchoolRequestSerializer},)
    def create(self, request):
        serializer = SchoolRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

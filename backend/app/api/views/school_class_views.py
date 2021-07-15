from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT

from drf_spectacular.utils import extend_schema

from api.permissions import PrincipalAccessPermission
from api.serializers.school_class_serializers import SchoolClassSerializer
from school.models import SchoolClass, School, Principal


class SchoolClassViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, PrincipalAccessPermission)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self, request):
        principal = Principal.objects.get(user=request.user)
        school = School.objects.get(school_principal=principal)
        return SchoolClass.objects.filter(school=school)

    @extend_schema(
        request=SchoolClassSerializer,
        responses={200: SchoolClassSerializer},)
    def list(self, request):
        queryset = self.get_queryset(request)
        serializer = SchoolClassSerializer(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=SchoolClassSerializer,
        responses={201: SchoolClassSerializer},)
    def create(self, request):
        serializer = SchoolClassSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = self.get_queryset(request)
        queryset.filter(pk=pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)
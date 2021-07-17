from api.utils import CyprusViewSet

from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema, OpenApiExample

from school.models import SchoolClass, School, Principal, Student, Subject

from api.permissions import PrincipalAccessPermission, PTAccessPermission, PTSAccessPermission
from api.serializers import (
    SchoolClassSerializer, SchoolRequestSerializer, StudentSerializer,
    StudentReadOnlySerializer
)


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


class SchoolClassViewSet(CyprusViewSet):
    queryset = SchoolClass.objects.none()
    permission_classes = (IsAuthenticated, PrincipalAccessPermission)
    permission_classes_by_action = {
        'list': [PTAccessPermission],
        'retrieve': [PTAccessPermission],
        'create': [PrincipalAccessPermission],
        'destroy': [PrincipalAccessPermission],
    }

    def get_queryset(self):
        request = self.request
        principal = Principal.objects.get(user=request.user)
        school = School.objects.get(school_principal=principal)
        return SchoolClass.objects.filter(school=school)

    @extend_schema(
        request=SchoolClassSerializer,
        responses={200: SchoolClassSerializer},)
    def list(self, request):
        queryset = self.get_queryset()
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
        queryset = self.get_queryset()
        queryset.filter(pk=pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)


class StudentViewSet(CyprusViewSet):
    queryset = Student.objects.none()
    permission_classes_by_action = {
        'list': [PTAccessPermission],
        'retrieve': [PTAccessPermission],
        'create': [PrincipalAccessPermission],
        'update': [PrincipalAccessPermission],
        'destroy': [PrincipalAccessPermission],
    }

    def get_queryset(self):
        role_class = self.request.user.get_role_class()
        role_instance = role_class.objects.get(user=self.request.user)
        return Student.objects.filter(school=role_instance.school)

    @extend_schema(
        request=StudentReadOnlySerializer,
        responses={200: StudentReadOnlySerializer}, )
    def list(self, request):
        serializer = StudentReadOnlySerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    @extend_schema(request=StudentSerializer)
    def create(self, request):
        serializer = StudentSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        request=StudentReadOnlySerializer,
        responses={200: StudentReadOnlySerializer}, )
    def retrieve(self, request, pk):
        queryset = self.get_queryset().filter(pk=pk).first()
        serializer = StudentReadOnlySerializer(queryset)
        return Response(serializer.data)

    @extend_schema(
        request=StudentSerializer,
        responses={200: StudentReadOnlySerializer}, )
    def update(self, request, pk):
        queryset = self.get_queryset().filter(pk=pk).first()
        serializer = StudentSerializer(queryset)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = self.get_queryset()
        queryset.filter(pk=pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)


class SubjectViewSet(CyprusViewSet):
    queryset = Subject.objects.none()
    permission_classes_by_action = {
        'list': [PTAccessPermission],
        'retrieve': [PTAccessPermission],
        'create': [PrincipalAccessPermission],
    }

    def get_queryset(self):
        role_class = self.request.user.get_role_class()
        role_instance = role_class.objects.get(user=self.request.user)
        return Subject.objects.filter(school=role_instance.school)

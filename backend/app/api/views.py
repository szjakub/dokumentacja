from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT

from drf_spectacular.utils import extend_schema

from api.permissions import (
    StudentAccessPermission, TeacherAccessPermission, PrincipalAccessPermission
)
from api.serializers import (
    SchoolRequestSerializer,  ClassSerializer, StudentSerializer,
    StudentReadOnlySerializer, SubjectSerializer, LessonSerializer
)
from school.models import SchoolClass, School, Student, Principal, Subject, Lesson


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


class ClassViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, PrincipalAccessPermission)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self, request):
        principal = Principal.objects.get(user=request.user)
        school = School.objects.get(school_principal=principal)
        return SchoolClass.objects.filter(school=school)

    @extend_schema(
        request=ClassSerializer,
        responses={200: ClassSerializer},)
    def list(self, request):
        queryset = self.get_queryset(request)
        serializer = ClassSerializer(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=ClassSerializer,
        responses={201: ClassSerializer},)
    def create(self, request):
        serializer = ClassSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = self.get_queryset(request)
        queryset.filter(pk=pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)


class StudentViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self, request):
        principal = Principal.objects.get(user=request.user)
        school = School.objects.get(school_principal=principal)
        return Student.objects.filter(school=school)

    @extend_schema(
        request=StudentReadOnlySerializer,
        responses={200: StudentReadOnlySerializer}, )
    @permission_classes([IsAuthenticated, PrincipalAccessPermission | TeacherAccessPermission])
    def list(self, request):
        queryset = self.get_queryset(request)
        serializer = StudentReadOnlySerializer(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=StudentSerializer,
        responses={200: StudentSerializer}, )
    @permission_classes([IsAuthenticated, PrincipalAccessPermission])

    def create(self, request):
        serializer = StudentSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @extend_schema(
        request=StudentSerializer,
        responses={200: StudentSerializer}, )
    @permission_classes([IsAuthenticated, PrincipalAccessPermission])
    def retrieve(self, request, pk):
        queryset = self.get_queryset(request).filter(pk=pk).first()
        return StudentSerializer(queryset)


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = LessonSerializer

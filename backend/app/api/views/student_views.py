from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST
from drf_spectacular.utils import extend_schema
from api.permissions import PrincipalAccessPermission, TeacherAccessPermission
from school.models import Student
from api.serializers.student_serializers import StudentSerializer, StudentReadOnlySerializer
from rest_condition import Or, And
from api.utils import CyprusViewSet


class StudentViewSet(CyprusViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes_by_action = {
        'list': [And(IsAuthenticated, Or(PrincipalAccessPermission, TeacherAccessPermission))],
        'retrieve': [And(IsAuthenticated, Or(PrincipalAccessPermission, TeacherAccessPermission))],
        'create': [And(IsAuthenticated, PrincipalAccessPermission)],
    }

    def get_queryset(self, request):
        role_class = request.user.get_role_class()
        role_instance = role_class.objects.get(user=request.user)
        return Student.objects.filter(school=role_instance.school)

    @extend_schema(
        request=StudentReadOnlySerializer,
        responses={200: StudentReadOnlySerializer}, )
    def list(self, request):
        queryset = self.get_queryset(request)
        serializer = StudentReadOnlySerializer(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=StudentSerializer,
        responses={200: StudentSerializer}, )
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
    def retrieve(self, request, pk):
        queryset = self.get_queryset(request).filter(pk=pk).first()
        return StudentSerializer(queryset)

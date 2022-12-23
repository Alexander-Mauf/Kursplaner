from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from . import serializers, models


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CustomerSerializer
    queryset = models.Customer.objects.order_by('-id')
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)


class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TeacherSerializer
    queryset = models.Teacher.objects.order_by('-id')
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)


class ClassViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClassSerializer
    queryset = models.Class.objects.order_by('-id')
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)


class AvailabilityViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AvailabilitySerializer
    queryset = models.Availability.objects.order_by('-id')
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)


class TimeslotViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TimeslotSerializer
    queryset = models.Timeslot.objects.order_by('-id')
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

class SkillsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SkillsSerializer
    queryset = models.Skills.objects.order_by('-id')
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from . import serializers, models, forms, tables
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.urls import reverse

class ClassCreateStep01View(FormView):
    template_name = 'kurse/kurs/class-create.html'
    form_class = forms.CustomerCreateForm

    def get_form(self, form_class=None):
        """Return an instance of the form to be used in this view."""
        if form_class is None:
            form_class = self.get_form_class()
        kwargs = self.get_form_kwargs()
        return form_class(**kwargs)

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        table = tables.CustomerTable(models.Customer.objects.all())
        return render(request, self.template_name, {
            'form': form,
            'table': table
        })

    def post(self, request, *args, **kwargs):

        form = self.get_form()
        error = False

        if not form.is_valid():
            error = 'ungültige Eingaben'






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

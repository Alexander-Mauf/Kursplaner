from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from . import serializers, models, forms
from django.views.generic.edit import FormView


class ClassCreateView(FormView):
    template_name = 'credentials/credential/create.html'
    form_class = forms.ClassCreateForm

    def get_form(self, form_class=None):
        """Return an instance of the form to be used in this view."""
        if form_class is None:
            form_class = self.get_form_class()
        kwargs = self.get_form_kwargs()
        kwargs['aktion'] = 'erstellen'
        return form_class(**kwargs)

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        sign = request.GET.get('sign')
        return render(request, self.template_name, {
            'form': form,
            'sign': sign,
            'create': True,
        })

    def post(self, request, *args, **kwargs):

        form = self.get_form()
        _, data = signer.loads_from_request(self.request)

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

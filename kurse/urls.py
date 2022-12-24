from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()

router.register(r'api/customers', views.CustomerViewSet)
router.register(r'api/teachers', views.TeacherViewSet)
router.register(r'api/availabilities', views.AvailabilityViewSet)
router.register(r'api/classes', views.ClassViewSet)
router.register(r'api/skills', views.SkillsViewSet)
router.register(r'api/timeslots', views.TimeslotViewSet)


urlpatterns = [
    #path("", views.CredentialListView.as_view(), name="credential_list"),
    path("create/", views.ClassCreateStep01View.as_view(), name="credential_create"),
    #path("<hash_id>/change/", views.CredentialUpdateView.as_view(), name="credential_update"),
]

urlpatterns += router.urls

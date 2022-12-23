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
]

urlpatterns += router.urls

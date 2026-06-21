from django.urls import include, path
from rest_framework  import routers

from tutorial.quickstart import views as quickstart_views
from tasks import views as task_views
from tasks.views import dashboard_view


router = routers.DefaultRouter()
router.register(r"users", quickstart_views.UserViewSet)
router.register(r"groups", quickstart_views.GroupViewSet)
router.register(r"tasks", task_views.TaskViewset, basename='tasks')

urlpatterns = [
    path("dashboard/", dashboard_view, name="dashboard"),
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


app_name = "shared"

router = DefaultRouter()
router.register(r"activity-logs", views.ActionModelViewSet)

urlpatterns = [path("", include(router.urls))]

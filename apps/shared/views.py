from django.shortcuts import render

from rest_framework import viewsets, mixins

from apps.agent.permissions import DynamicActionPermission
from .models import ActionModel
from .serializers import ActionModelSerializer


class ActionModelViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
    queryset = ActionModel.objects.order_by("created_at")
    serializer_class = ActionModelSerializer
    filterset_fields = ("object_id", "content_type", )
    permission_classes = (DynamicActionPermission, )

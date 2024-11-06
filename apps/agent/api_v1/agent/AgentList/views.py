from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django_filters import rest_framework as filters
from rest_framework.generics import ListAPIView

from apps.agent.filters import AgentFilter
from apps.agent.models import Agent
from apps.agent.permissions import IsSupervisorPermission, ReadOnlyPermission
from .serializers import AgentListSerializer


class AgentListAPIView(ListAPIView):
    queryset = Agent.objects.order_by("created_at")
    serializer_class = AgentListSerializer
    permission_classes = (
        IsSupervisorPermission | ReadOnlyPermission,
    )
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = AgentFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        
        query_params = self.request.query_params

        username = query_params.get("username")
        first_name = query_params.get("first_name")
        last_name = query_params.get("last_name")
        is_active = query_params.get("is_active")
        role = query_params.get("role")
        extension = query_params.get("extension")

        if username:
            queryset = queryset.filter(username__icontains=username)
        if first_name:
            queryset = queryset.filter(last_name__icontains=last_name)
        if is_active:
            queryset = queryset.filter(is_active__icontains=is_active)
        if role:
            queryset = queryset.filter(role__icontains=role)
        if extension:
            queryset = queryset.filter(extension__icontains=extension)
        return queryset
    
    @swagger_auto_schema(
        manual_parameters=[
             openapi.Parameter(
                "username",
                openapi.IN_QUERY,
                required=False,
                description="Agent's username",
                type="string",
            ),
            openapi.Parameter(
                "first_name",
                openapi.IN_QUERY,
                required=False,
                description="Agent's first name",
                type="string",
            ),
            openapi.Parameter(
                "last_name",
                openapi.IN_QUERY,
                required=False,
                description="Agent's last name",
                type="string",
            ),
            openapi.Parameter(
                "is_active",
                openapi.IN_QUERY,
                required=False,
                description="Agent activation status",
                type="boolean",
            ),
            openapi.Parameter(
                "role",
                openapi.IN_QUERY,
                required=False,
                description="Agent's role",
                type="string",
            ),
            openapi.Parameter(
                "extension",
                openapi.IN_QUERY,
                required=False,
                description="Agent's extension",
                type="string",
            ),
        ]
    )

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


__all__ = ("AgentListAPIView", )

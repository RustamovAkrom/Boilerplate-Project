from rest_framework.generics import RetrieveUpdateDestroyAPIView, UpdateAPIView

from apps.agent.models import Agent
from apps.agent.permissions import IsAdminPermission
from .serializers import AgentUpdateSerializer


class UpdateProfileView(RetrieveUpdateDestroyAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentUpdateSerializer
    permission_classes = (IsAdminPermission, )

__all__ = ("UpdateProfileView", )

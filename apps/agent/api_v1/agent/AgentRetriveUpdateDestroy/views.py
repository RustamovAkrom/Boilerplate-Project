from rest_framework.generics import RetrieveUpdateDestroyAPIView, UpdateAPIView

from .serializers import AgentRetriveUpdateDestroySerializer, ChangePasswordSerializer

from apps.agent.models import Agent
from apps.shared.tasks import action_log


class AgnetRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentRetriveUpdateDestroySerializer

    def perform_destroy(self, instance):
        request = self.request
        agent = request.user

        action_log(
            instance, request, "delete", "112", old_value=agent.username, new_value=None
        )
        super().perform_destroy(instance)

    
class ChangePasswordVeiw(UpdateAPIView):
    queryset = Agent.objects.all()
    serializer_class = ChangePasswordSerializer()

__all__ = ("AgnetRetriveUpdateDestroyAPIView", "ChangePasswordVeiw", )

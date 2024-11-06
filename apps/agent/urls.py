from django.urls import path

from apps.agent.api_v1.agent import AgentListAPIView
app_name = "agent"

urlpatterns = [
    path('', AgentListAPIView.as_view(), name="agent-list"),
]

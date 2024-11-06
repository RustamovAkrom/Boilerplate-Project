from django.urls import path

from apps.agent.api_v1.agent import (
    AgentListAPIView, 
    AgentRetriveUpdateDestroyAPIView,
    ChangePasswordAPIView,
    UpdateProfileAPIView,
)

app_name = "agent"

urlpatterns = [
    path('', AgentListAPIView.as_view()),
    path('<int:pk>/', AgentRetriveUpdateDestroyAPIView.as_view()),
    path('change-password', ChangePasswordAPIView.as_view(), name="agent-change-password"),
    path('update-profile', UpdateProfileAPIView.as_view(), name="agent-update-profile"),
]

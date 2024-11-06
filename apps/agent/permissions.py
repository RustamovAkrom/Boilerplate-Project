from django.contrib.auth.models import Group

from rest_framework.permissions import BasePermission, SAFE_METHODS

from apps.agent.models import AgentRoleChoice


class DynamicActionPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated
        
        model_name = view.queryset.model._meta.model_name

        method_to_permision = {
            "GET": "view",
            "POST": "add",
            "PUT": "change",
            "PATCH": "change",
            "DELETE": "delete",
        }

        permission_type = method_to_permision.get(request.method)

        if not permission_type:
            return False
        
        codename = f"{permission_type}_{model_name}"

        if request.user.user_permissions.filter(codename=codename).exists():
            return True
        else:
            return False


class IsOwnerPermission(BasePermission):
    
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
    
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsSupervisorPermission(BasePermission):
    
    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.role == AgentRoleChoice.SUPERVISOR.value
        )
    
    def has_object_permission(self, request, view, obj):
        return request.user.role == AgentRoleChoice.SUPERVISOR.value


class ReadOnlyOrSupervisorPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated
            or request.user.role == AgentRoleChoice.SUPERVISOR.value
        )
    

class ReadOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsAgentPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return bool(
            request.user.role == AgentRoleChoice.AGENT
            or request.user.role == AgentRoleChoice.SUPERVISOR
        )


class IsManagerPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return bool(request.user.role == AgentRoleChoice.MANAGER)


class IsAdminPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return bool(request.user.role == AgentRoleChoice.ADMIN)

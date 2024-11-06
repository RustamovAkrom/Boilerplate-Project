from .models import Agent


class UsernameAuthBackend:
    def authenticate(self, request, username=None, password=None, extension=None):
        try:
            user = Agent.objects.get(username=username)
            if user.check_password(password):
                return user
            return None
        except (Agent.DoesNotExist, Agent.MultipleObjectsReturned):
            return None

    def get_user(self, user_id):
        try:
            return Agent.objects.get(pk=user_id)
        except Agent.DoesNotExist:
            return None
        

class ExtensionAuthBackend:
    def authenticate(self, request, password=None, extension=None):
        try:
            user = Agent.objects.get(extension=extension)
            if user.check_password(password):
                return user
            return None
        except (Agent.DoesNotExist, Agent.MultipleObjectsReturned):
            return None
        
    def get_user(self, user_id):
        try:
            return Agent.objects.get(pk=user_id)
        except Agent.DoesNotExist:
            return None

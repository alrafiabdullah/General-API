from rest_framework import authentication
from rest_framework import exceptions

from .models import VerificationCode


class APIKEYAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        api_key = request.META.get('HTTP_API_KEY')
        if not api_key:
            raise exceptions.AuthenticationFailed('API Key not found')

        try:
            code = VerificationCode.objects.get(code=api_key, validity=True)
        except:
            raise exceptions.AuthenticationFailed(
                'API Key does not exist or inactive')

        return (code, None)

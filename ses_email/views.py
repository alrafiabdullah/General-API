from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.conf import settings
from django.core.mail import EmailMessage

from .models import VerificationCode
from .serializers import EmailSerializer


# Create your views here.
class SesEmail(APIView):
    description = "Send an email to a user"
    serializer_class = EmailSerializer

    def get(self, request):
        return Response({"status": "Email Service Up & Running!"}, status=status.HTTP_200_OK)

    def post(self, request):
        api_key = request.data['api_key']

        if not VerificationCode.objects.filter(code=api_key, validity=True):
            return Response({"error": f"Invalid API Key, {api_key}\\nEither expired or does not exist!"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = EmailMessage(
            subject=serializer.validated_data['subject'],
            body=serializer.validated_data["message"],
            from_email=settings.EMAIL_FROM,
            to=[serializer.validated_data["email"]],
            bcc=[settings.EMAIL_BCC],
        )

        email.send()
        return Response({"message": f"Email sent to {serializer.validated_data['email']}"}, status=status.HTTP_200_OK)

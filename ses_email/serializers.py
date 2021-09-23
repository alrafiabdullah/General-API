from rest_framework import serializers


class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=100)
    message = serializers.CharField(max_length=999)

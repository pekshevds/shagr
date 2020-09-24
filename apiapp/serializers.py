from rest_framework import serializers

class GoodSerializer(serializers.Serializer):

    slug = serializers.CharField(max_length=36)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
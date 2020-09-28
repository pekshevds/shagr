from rest_framework import serializers

class GoodSerializer(serializers.Serializer):

    uid_1c = serializers.CharField(max_length=36)
    name = serializers.CharField(max_length=255)
    art = serializers.CharField(max_length=25)
    description = serializers.CharField()
    full_name = serializers.CharField()
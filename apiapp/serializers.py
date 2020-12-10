from rest_framework import serializers

class GoodSerializer(serializers.Serializer):

    uid_1c = serializers.CharField(max_length=36)
    code_1c = serializers.CharField(max_length=11)
    name = serializers.CharField(max_length=255)
    art = serializers.CharField(max_length=25)
    description = serializers.CharField()
    full_name = serializers.CharField()
    category_uid_1с = serializers.CharField(max_length=36)
    price = serializers.DecimalField(default=0, max_digits=15, decimal_places=2)
    quant = serializers.DecimalField(default=0, max_digits=15, decimal_places=3)
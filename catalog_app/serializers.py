from typing import Any
from rest_framework import serializers
from catalog_app.models import Category, Good, Producer
from rest_framework_recursive.fields import RecursiveField


def fill_by_link(
    obj: object,
    attr_name: str,
    validated_data: dict[str, Any],
    serializer: serializers.Serializer,
) -> None:
    if attr_name in validated_data:
        setattr(obj, attr_name, None)
    data = validated_data.get(attr_name)
    if data:
        ser = serializer(data=data)
        if ser.is_valid():
            setattr(obj, attr_name, ser.save())


class ProducerSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)

    def create(self, validated_data: dict[str, Any]) -> Producer:
        obj, _ = Producer.objects.get_or_create(id=validated_data.get("id"))
        obj.name = validated_data.get("name", obj.name)
        obj.save()
        return obj


class CategorySerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    parent = RecursiveField(allow_null=True, required=False)
    image1 = serializers.ImageField(use_url=True, read_only=True)
    seo_cleaned_title = serializers.CharField(required=False, allow_blank=True)
    seo_cleaned_description = serializers.CharField(required=False, allow_blank=True)
    seo_cleaned_keywords = serializers.CharField(required=False, allow_blank=True)

    def create(self, validated_data: dict[str, Any]) -> Category:
        obj, _ = Category.objects.get_or_create(id=validated_data.get("id"))
        obj.name = validated_data.get("name", obj.name)
        obj.seo_title = validated_data.get("seo_title", obj.seo_title)
        obj.seo_description = validated_data.get("seo_description", obj.seo_description)
        obj.seo_keywords = validated_data.get("seo_keywords", obj.seo_keywords)
        fill_by_link(obj, "parent", validated_data, CategorySerializer)
        obj.save()
        return obj


class GoodSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    art = serializers.CharField(max_length=50, required=False, allow_blank=True)
    code = serializers.CharField(max_length=11, required=False, allow_blank=True)
    category = CategorySerializer(required=False, allow_null=True)
    producer = ProducerSerializer(required=False, allow_null=True)
    image1 = serializers.ImageField(use_url=True, read_only=True)
    image2 = serializers.ImageField(use_url=True, read_only=True)
    image3 = serializers.ImageField(use_url=True, read_only=True)
    image4 = serializers.ImageField(use_url=True, read_only=True)
    description = serializers.CharField(required=False, allow_blank=True)
    seo_title = serializers.CharField(required=False, allow_blank=True)
    seo_description = serializers.CharField(required=False, allow_blank=True)
    seo_keywords = serializers.CharField(required=False, allow_blank=True)

    def create(self, validated_data: dict[str, Any]) -> Good:
        obj, _ = Good.objects.get_or_create(id=validated_data.get("id"))
        obj.name = validated_data.get("name", obj.name)
        obj.art = validated_data.get("art", obj.art)
        obj.code = validated_data.get("code", obj.code)
        obj.description = validated_data.get("description", obj.description)
        obj.seo_title = validated_data.get("seo_title", obj.seo_title)
        obj.seo_description = validated_data.get("seo_description", obj.seo_description)
        obj.seo_keywords = validated_data.get("seo_keywords", obj.seo_keywords)
        fill_by_link(obj, "category", validated_data, CategorySerializer)
        fill_by_link(obj, "producer", validated_data, ProducerSerializer)
        obj.save()
        return obj

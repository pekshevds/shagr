from typing import Any
from rest_framework import serializers
from catalog_app.models import Category, Good


class CategorySerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    image = serializers.ImageField(use_url=True, read_only=True)
    seo_cleaned_title = serializers.CharField(
        max_length=2048, required=False, allow_blank=True
    )
    seo_cleaned_description = serializers.CharField(
        max_length=2048, required=False, allow_blank=True
    )
    seo_cleaned_keywords = serializers.CharField(
        max_length=2048, required=False, allow_blank=True
    )

    def create(self, validated_data: dict[str, Any]) -> Category:
        category, _ = Category.objects.get_or_create(id=validated_data.get("id"))
        category.name = validated_data.get("name", category.name)
        category.seo_title = validated_data.get("seo_title", category.seo_title)
        category.seo_description = validated_data.get(
            "seo_description", category.seo_description
        )
        category.seo_keywords = validated_data.get(
            "seo_keywords", category.seo_keywords
        )
        category.save()
        return category


class GoodSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    art = serializers.CharField(max_length=50, required=False, allow_blank=True)
    code = serializers.CharField(max_length=11, required=False, allow_blank=True)
    category = CategorySerializer(required=False, allow_null=True)
    image = serializers.ImageField(use_url=True, read_only=True)
    image1 = serializers.ImageField(use_url=True, read_only=True)
    image2 = serializers.ImageField(use_url=True, read_only=True)
    image3 = serializers.ImageField(use_url=True, read_only=True)
    image4 = serializers.ImageField(use_url=True, read_only=True)
    description = serializers.CharField(
        max_length=2048, required=False, allow_blank=True
    )
    seo_title = serializers.CharField(max_length=2048, required=False, allow_blank=True)
    seo_description = serializers.CharField(
        max_length=2048, required=False, allow_blank=True
    )
    seo_keywords = serializers.CharField(
        max_length=2048, required=False, allow_blank=True
    )

    def create(self, validated_data: dict[str, Any]) -> Good:

        good, _ = Good.objects.get_or_create(id=validated_data.get("id"))
        good.name = validated_data.get("name", good.name)
        good.art = validated_data.get("art", good.art)
        good.code = validated_data.get("code", good.code)
        good.description = validated_data.get("description", good.description)
        good.seo_title = validated_data.get("seo_title", good.seo_title)
        good.seo_description = validated_data.get(
            "seo_description", good.seo_description
        )
        good.seo_keywords = validated_data.get("seo_keywords", good.seo_keywords)

        category_data = validated_data.get("category")
        if category_data:
            category_serializer = CategorySerializer(data=category_data)
            if category_serializer.is_valid():
                good.category = category_serializer.save()
        good.save()
        return good

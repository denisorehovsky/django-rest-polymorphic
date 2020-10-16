from rest_framework import serializers

from rest_polymorphic.serializers import PolymorphicSerializer

from tests.models import BlogBase, BlogOne, BlogTwo, BlogThree, Webpage


class BlogBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogBase
        fields = ('name', 'slug')


class BlogOneSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogOne
        fields = ('name', 'slug', 'info')


class BlogTwoSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogTwo
        fields = ('name', 'slug')


class BlogThreeSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogThree
        fields = ('name', 'slug', 'info', 'about')


class BlogPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        BlogBase: BlogBaseSerializer,
        BlogOne: BlogOneSerializer,
        BlogTwo: BlogTwoSerializer,
        BlogThree: BlogThreeSerializer
    }


class WebpageSerializer(serializers.ModelSerializer):
    blog = BlogPolymorphicSerializer()

    class Meta:
        model = Webpage
        fields = ('url', 'blog')

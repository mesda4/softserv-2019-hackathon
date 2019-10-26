import io
from pprint import pprint
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.validators import UniqueTogetherValidator
from needs.models import NeedType, OrpanageNeed


class NeedTypeSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        pprint(validated_data)
        return NeedType.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    class Meta:
        model = NeedType
        fields = '__all__'


class NeedSerializer(serializers.ModelSerializer):
    # id_type = NeedTypeSerializer(many=True)
    def create(self, validated_data):
        pprint(validated_data)
        return OrpanageNeed.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    class Meta:
        model = OrpanageNeed
        fields = '__all__'
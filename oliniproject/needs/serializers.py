import io
from pprint import pprint
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.validators import UniqueTogetherValidator
from needs.models import *
from animals.models import *


class NeedTypeSerializer(serializers.ModelSerializer):
    type_name = serializers.CharField(source='type.name', read_only=True)
    pet_name = serializers.CharField(source='animal.name', read_only=True)

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


class AnimalNeedSerializer(serializers.ModelSerializer):

    # type_name = serializers.CharField(source='type.name', read_only=True)
    # pet_name = serializers.CharField(source='animal.name', read_only=True)

    def create(self, validated_data):
        pprint(validated_data)
        return AnimalNeed.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        # instance.id_animal = validated_data.get('id_animal', instance.id_animal)

        instance.save()
        return instance

    def to_representation(self, instance):
        response = {}
        data = super(AnimalNeedSerializer, self).to_representation(instance)
        response = data
        response['pet_name'] = ''
        if data['id_animal'] != None:
            response['pet_name'] = str(Animal.objects.filter(uuid=data['id_animal']).get())
        if data['id_type'] != None:
            response['type_name'] = str(NeedType.objects.filter(pk=data['id_type']).get())
            pprint(response['type_name'])

        return response

    class Meta:
        model = AnimalNeed
        fields = '__all__'


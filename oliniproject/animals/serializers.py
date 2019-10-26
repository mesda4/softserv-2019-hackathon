from rest_framework import serializers
from data.models import *
from animals.models import *
from django.conf import settings


class AnimalTypeSerializer(serializers.ModelSerializer):
    type = serializers.CharField(required=True)
    class Meta:
        model = AnimalType
        fields = ['type']


class AnimalSerializer(serializers.ModelSerializer):
    uuid=serializers.ReadOnlyField()
    name=serializers.CharField(required=True)
    description=serializers.CharField(required=False)
    id_type = AnimalTypeSerializer(many=False, required=False)
    status = serializers.CharField(required=False)
    #animal_type = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    photo_path = serializers.CharField(required=False)

    class Meta:
        model=Animal
        fields=['uuid', 'name', 'description', 'id_type', 'status', 'photo_path', ]

    def create(self, validated_data):
        animal = Animal.create_animal(name = validated_data.get('name'), description=validated_data.get('description'), id_type=validated_data.get('id_type'))
        return animal

    def to_representation(self, instance):
        response={}
        #data=super(CourseSerializer, self).to_representation(instance)
        

class AnimalsSerializer(serializers.ModelSerializer):
    uuid=serializers.ReadOnlyField()
    description=serializers.CharField(required=False)
    status = serializers.CharField(required=False)
    photo_path = serializers.CharField(required=False)

    class Meta:
        model=Animal
        fields=['uuid', 'name', 'description', 'id_type', 'status', 'photo_path', ]

    def to_representation(self, instance):
        response = {}
        data = super(AnimalsSerializer, self).to_representation(instance)
        #url = data['photo_path'] + AnimalPhoto.objects.filter(animal=data['uuid']).first().photo
        url = data['photo_path'] + AnimalPhoto.objects.filter(animal=Animal.objects.get(uuid=data['uuid'])).first().photo

        response['status'] = data['status']
        response['photo'] = url
        response['uuid'] = data['uuid']

        return response

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Animal
        fields=['photo', ]

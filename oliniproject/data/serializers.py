from rest_framework import serializers
from data.models import *

class UserSerializer(serializers.ModelSerializer):

    date_joined = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name',
                  'date_joined', 'password', 'is_staff')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        try:
            person = User.objects.get(email=value)
            raise serializers.ValidationError("Email already exist")
        except User.DoesNotExist:
            pass
        return value

    def create(self, validated_data):
        user = User(email=validated_data.get('email'), password=validated_data.get('password'), first_name=validated_data.get('first_name'), last_name=validated_data.get('last_name'))
        user.save()
        return user






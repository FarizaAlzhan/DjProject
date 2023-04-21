from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from project.models import *
class BookSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Books
        fields = ('__all__')

class Training1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Training1
        fields = ('__all__')

class Training2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Training2
        fields = ('__all__')
class Training_manager1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Training_manager1
        fields = ('__all__')
class Training_manager2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Training_manager2
        fields = ('__all__')
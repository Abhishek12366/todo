from dataclasses import field, fields
from importlib.metadata import files
from pyexpat import model
from rest_framework import serializers
from api.models import Todos
from django.contrib.auth.models import User

class Todoserializer(serializers.ModelSerializer):
    status=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Todos
        fields=["task_name","user","status"]

    #TO CREATE TODOS BY SPECIFIC USERS(C)

    def create(self, validated_data):
        usr=self.context.get("user")
        return Todos.objects.create(**validated_data,user=usr)

class Registrationserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.utils import model_meta
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
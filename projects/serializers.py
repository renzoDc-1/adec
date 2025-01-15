from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','title', 'description', 'technology', 'create_at')
        read_only_fields = ('create_at', ) # hace que el campo create_at solo sea de lectura
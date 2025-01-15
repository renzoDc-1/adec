from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()  #consulta todos los datos de una tabla
    permissions_classes = [permissions.AllowAny] # quien tiene permiso 
    serializer_class = ProjectSerializer
from rest_framework import viewsets
from .models import Node
from .serializers import NodeSerializer

class NodeViewsets(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
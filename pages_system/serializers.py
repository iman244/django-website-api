from rest_framework import serializers
from .models import Node
from rest_framework_recursive.fields import RecursiveField
        
class NodeSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)
    
    class Meta:
        model = Node
        fields = ['key', 'children']
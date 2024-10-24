from django.contrib import admin
from .models import Node
from mptt.admin import MPTTModelAdmin

admin.site.register(Node, MPTTModelAdmin)
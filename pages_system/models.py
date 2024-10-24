from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey

class Node(MPTTModel):
    key = models.CharField(_("key"), max_length=255, unique=True, primary_key=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['key']


class NodeDetail(models.Model):
    order = models.SmallIntegerField(_("order"), default=0)

    class Meta:
        abstract = True


class Text(NodeDetail):
    node = models.ManyToManyField(Node, verbose_name=_("texts"), related_name='texts')
    text = models.CharField(_("text"), max_length=255)

    def __str__(self):
        return self.text
from django.db import models
from django.utils.translation import gettext_lazy as _

class Node(models.Model):
    key = models.CharField(_("key"), max_length=255, primary_key=True, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.key
    

class NodeDetail(models.Model):
    order = models.SmallIntegerField(_("order"), default=0)

    class Meta:
        abstract = True


class Text(NodeDetail):
    node = models.ManyToManyField(Node, verbose_name=_("texts"), related_name='texts')
    text = models.CharField(_("text"), max_length=255)

    def __str__(self):
        return self.text
from rest_framework import routers
from .views import NodeViewsets

router = routers.DefaultRouter()
router.register(r'nodes', NodeViewsets)

urlpatterns = router.urls
from .views import CommunicationSchedulingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(
    r'scheduling',
    CommunicationSchedulingViewSet,
    basename='scheduling'
)
urlpatterns = router.urls

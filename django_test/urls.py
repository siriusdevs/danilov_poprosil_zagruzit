from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet, EquipmentViewSet

router = DefaultRouter()
router.register(r'persons', PersonViewSet)
router.register(r'equipments', EquipmentViewSet)

urlpatterns = [
    path('api/', include(router.urls), name='api'),
]
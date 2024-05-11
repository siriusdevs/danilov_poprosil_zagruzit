from rest_framework.viewsets import ModelViewSet
from .models import Person, Equipment
from .serializers import PersonSerializer, EquipmentSerializer

class PersonViewSet(ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class EquipmentViewSet(ModelViewSet):
    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.all()

from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Person, Equipment


class PersonSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class EquipmentSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'
from rest_framework import serializers
from .models import Drink
from rest_framework import permissions
from rest_framework_api_key.permissions import HasAPIKey

class DrinkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id','name','description']
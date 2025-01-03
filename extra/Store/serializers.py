from rest_framework import serializers
from Store.models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields='__all__'

class FictionSerializer(serializers.ModelSerializer):
    class Meta:
        model=fiction
        fields='__all__'


class contactserializer(serializers.ModelSerializer):
    class Meta:
        model=contact
        fields='__all__'

               
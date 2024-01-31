from comp_app.models import Computer
from rest_framework import serializers

class CompSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = ['title', 'info', 'price']


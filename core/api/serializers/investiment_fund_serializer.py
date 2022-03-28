# Rest Framework
from rest_framework import serializers

# Models
from core.models import InvestimentFund


class InvestmentFundInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestimentFund
        fields = '__all__'
        read_only_fields = ['created_at', 'id']


class InvestimentFundOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestimentFund
        fields = '__all__'
        read_only_fields = ['created_at', 'id']
        
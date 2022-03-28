# Models
from core.models import InvestimentFund

# Utils
from django.db import transaction
from django.utils import timezone

# Selectors
from core.selectors import InvestimentFundSelector


class InvestimentFundService:
    @transaction.atomic
    def create(self, validated_data):
        """
        Create a Investment Fund instance with the given data.

        Returns:
            [investiment_fund]: [the created Investiment Fund object]
        """

        # Create Investiment Fund object
        investiment_fund = InvestimentFund.objects.create(**validated_data)

        return investiment_fund

    @transaction.atomic
    def update(self, validated_data, id):
        """
        Update a Investiment Fund instance with the given data.

        Args:
            validated_data (Serializer.validated_data): [Data that will be used in the update]
            id (Int): [The Investiment Fund id] 

        Returns:
            [investiment_fund]: [the updated Investiment Fund object]
        """

        investiment_fund_selector = InvestimentFundSelector()

        investiment_fund = investiment_fund_selector.get_investiment_fund_by_id(id=id)

        for key in validated_data:
            setattr(investiment_fund, key, validated_data[key])

        investiment_fund.updated_at = timezone.now()
        investiment_fund.save()

        return investiment_fund

    @transaction.atomic
    def delete(self, id):
        """ 
        Delete a Investiment Fund

        Args:
            id (django id): [the Investiment Fund id, that is the primary key in the database]
        """

        investiment_fund_selector = InvestimentFundSelector()

        investiment_fund = investiment_fund_selector.get_investiment_fund_by_id(id=id)

        investiment_fund.deleted_at = timezone.now()
        investiment_fund.save()

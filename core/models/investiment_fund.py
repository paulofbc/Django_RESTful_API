"""
This module contains the Django model for a Momentum Investiment Fund
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models.base_model import BaseModel
from core.utils import (
    FundType, 
    FundClass, 
    FundSubclass
)


class InvestimentFund(BaseModel):
    """
    This class contains a model definition
    """

    class Meta:
        """
        This meta class contains information to display and store data related to this model
        """

        verbose_name = _('Investiment Fund')
        verbose_name_plural = _(' Investiment Funds')
        db_table = "investiment_fund"

    name = models.CharField(max_length=150, null=True, blank=True)
    administrator = models.CharField(max_length=100, null=True, blank=True)
    manager = models.CharField(max_length=100, null=True, blank=True)
    cnpj = models.CharField(max_length=18, null=True, blank=True)

    benchmark = models.CharField(max_length=25, null=True, blank=True)

    fund_type = models.CharField(
        max_length=25, default=FundType.FUND_TYPE_1, choices=FundType.choices(), null=True, blank=True)
    fund_class = models.CharField(
        max_length=25, default=FundClass.FUND_CLASS_1, choices=FundClass.choices(), null=True, blank=True)
    fund_subclass = models.CharField(
        max_length=25, default=FundSubclass.FUND_SUBCLASS_1, choices=FundSubclass.choices(), null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

# Rest Framework
from rest_framework import routers

from django.urls import path, include
from core import views

from core.api.views import (
    InvestimentFundApi
)

urlpatterns = [
    path('', views.home, 
        name="home"),
    path('api/investiment-fund', InvestimentFundApi.as_view(), 
        name="all_investiment_fund"),
    path('api/investiment-fund/<int:id>', InvestimentFundApi.as_view(), 
        name="investiment_fund_by_id")
]

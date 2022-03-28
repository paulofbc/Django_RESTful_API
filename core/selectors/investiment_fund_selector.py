# Models
from core.models import InvestimentFund


class InvestimentFundSelector:
    def get_investiment_fund_by_id(self, id):
        """
        Get Investiment Fund by id

        Args:
            id (Django id): [the object id, that is the primary key in the database]

        Raises:
            ObjectDoesNotExist: [No Investiment Fund with this id]

        Returns:
            [investiment_fund]: [Investiment Fund Object]
        """

        return InvestimentFund.objects.get(pk=id)

    def get_all_investiment_funds(self):
        """
        Get Investiment Fund

        Returns:
            [investiment_fund]: [Investiment Fund Objects list]
        """

        return InvestimentFund.objects.all()

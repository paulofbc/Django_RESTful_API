# Traceback
import traceback

# Rest Framework
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

# Utils
from core.utils.logging_utils import log_error_messages

# Django
from django.core.exceptions import ObjectDoesNotExist

# Selector
from core.selectors import InvestimentFundSelector

# Service
from core.services import InvestimentFundService

# Serializer
from core.api.serializers import (
    InvestimentFundOutputSerializer,
    InvestmentFundInputSerializer
)


class InvestimentFundApi(GenericAPIView):
    http_method_names = ['get', 'post', 'put', 'delete']
    permissions_classes = [permissions.IsAuthenticated]

    def get(self, request, id=None):
        """
        Get all the Investiment Fund by company or get an Investiment Fund by id.

        Args:
            request (http-request): [http-request object]
            id ([Django ID]): [django id of the Investiment Fund]. Defaults to None.

        Returns:
            [Response]: [http-response with all the Investiment Funds or the selected Investiment Fund]
        """

        try:
            investiment_fund_selector = InvestimentFundSelector()

            if id is not None:
                investiment_fund = investiment_fund_selector.get_investiment_fund_by_id(id=id)

                return Response(InvestimentFundOutputSerializer(investiment_fund).data, status=status.HTTP_200_OK)

            investiment_fund_list = investiment_fund_selector.get_all_investiment_funds()

            return Response(InvestimentFundOutputSerializer(investiment_fund_list, many=True).data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist as ex:
            log_error_messages(traceback.format_exc())
            return Response({"msg": "ERROR_OBJECT_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            log_error_messages(traceback.format_exc())
            return Response({"msg": "INTERNAL_SERVER_ERROR"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        """
        Create a Investiment Fund object.

        Args:
            request (http-request): [the http request object]

        Returns:
            [Http-Response]: [An http response with data or an error message]
        """

        try:
            serializer = InvestmentFundInputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            investiment_fund_service = InvestimentFundService()
            investiment_fund = investiment_fund_service.create(validated_data=serializer.validated_data)

            return Response(InvestimentFundOutputSerializer(investiment_fund).data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist as ex:
            log_error_messages(traceback.format_exc())
            return Response({"msg": "ERROR_OBJECT_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            log_error_messages(traceback.format_exc())
            return Response({"msg": "INTERNAL_SERVER_ERROR"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id):
        """
        Update Investiment Fund object.

        Args:
            request (http-request): [the http request object]
            id (django id): [the object id, that is the primary key in the database]

        Returns:
            [Http-Response]: [An http response with data or an error message]
        """

        try:
            serializer = InvestmentFundInputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            investiment_fund_service = InvestimentFundService()
            investiment_fund = investiment_fund_service.update(
                validated_data=serializer.validated_data, id=id)

            return Response(InvestimentFundOutputSerializer(investiment_fund).data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist as ex:
            log_error_messages(traceback.format_exc())
            return Response({"msg": "ERROR_OBJECT_NOT_FUND"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            log_error_messages(traceback.format_exc())
            return Response({"msg": "INTERNAL_SERVER_ERROR"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, id):
        """
        Delete a Investiment Fund

        Args:
            request (http-request): [http-request object]
            id (django id): [the object id, that is the primary key in the database]
            id ([Django ID]): [django id of the Investiment Fund].

        Returns:
            [Response]: [http-response with status 204]
        """

        try:
            investiment_fund_service = InvestimentFundService()
            investiment_fund = investiment_fund_service.delete(id=id)

            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist as ex:
            log_error_messages(traceback.format_exc())
            return Response({"msg": "ERROR_OBJECT_NOT_FUND"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            log_error_messages(traceback.format_exc())
            return Response({"msg": "INTERNAL_SERVER_ERROR"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

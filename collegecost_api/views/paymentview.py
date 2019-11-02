"""View module for handling requests about payment"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from collegecost_api.models import *

class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  PaymentModel
        url = serializers.HyperlinkedIdentityField(
            view_name='payment',
            lookup_field='id'
        )
        fields = ('id', 'amount', 'paymenttype', 'year')
        depth = 2

class Payment(ViewSet):
    queryset = PaymentModel.objects.all()
    def create(self, request):

        """Handle POST operations
        Returns:
            Response -- JSON serialized Attraction instance
        """
        new_payment = PaymentModel()
        new_payment.amount = request.data["amount"]
        new_payment.paymenttype = PaymentTypeModel.objects.get(pk=request.data["paymenttype"])
        new_payment.year = YearModel.objects.get(pk=request.data["year"])
        new_payment.save()
        serializer = PaymentSerializer(new_payment, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single park area
        Returns:
            Response -- JSON serialized park area instance
        """
        try:
            payment = PaymentModel.objects.get(pk=pk)
            serializer = PaymentSerializer(payment, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single product are
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            payment = PaymentModel.objects.get(pk=pk)
            payment.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except PaymentModel.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to payment types resource

        Returns:
            Response -- JSON serialized list of payment types
        """
        payments = PaymentModel.objects.all()
        amount = self.request.query_params.get('amount', None)
        paymenttype = self.request.query_params.get('paymenttype', None)
        year = self.request.query_params.get('year', None)

        serializer = PaymentSerializer(
            payments, many=True, context={'request': request})
        return Response(serializer.data)

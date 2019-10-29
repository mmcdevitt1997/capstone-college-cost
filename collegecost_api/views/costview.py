"""View module for handling requests about cost """
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from collegecost_api.models import *

class CostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CostModel
        url = serializers.HyperlinkedIdentityField(
            view_name='costtype',
            lookup_field='id'
        )
        fields = ('id', 'url', 'amount', 'paymenttype')
        depth = 0

class Cost(ViewSet):
    queryset = CostModel.objects.all()
    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized Attraction instance
        """
        new_cost = CostTypeModel()
        new_cost.amount = request.data["amount"]
        new_cost.costtype = request.data["costtype"]
        serializer = CostSerializer(new_cost, context={'request': request})
        return Response(serializer.data)

def retrieve(self, request, pk=None):
    """Handle GET requests for single park area
    Returns:
        Response -- JSON serialized park area instance
    """
    try:
       cost = CostModel.objects.get(pk=pk)
       serializer = CostSerializer(cost, context={'request': request})
       return Response(serializer.data)
    except Exception as ex:
        return HttpResponseServerError(ex)

def destroy(self, request, pk=None):
    """Handle DELETE requests for a single product are
    Returns:
        Response -- 200, 404, or 500 status code
    """
    try:
        cost = CostModel.objects.get(pk=pk)
        cost.delete()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    except CostModel.DoesNotExist as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    except Exception as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def list(self, request):
    """Handle GET requests to payment types resource

    Returns:
        Response -- JSON serialized list of payment types
    """
    costs = CostModel.object.all()
    amount = self.request.query_params.get('amount', None)
    costtype = self.request.query_params.get('paymenttype', None)

    serializer = CostSerializer(
        costs, many=True, context={'request': request})
    return Response(serializer.data)

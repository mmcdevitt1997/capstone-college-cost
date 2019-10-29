"""View module for handling requests about cost type"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from collegecost_api.models import *

class CostTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CostTypeModel
        url = serializers.HyperlinkedIdentityField(
            view_name='costtype',
            lookup_field='id'
        )
        fields = ('id', 'url', 'name', 'color')


class CostType(ViewSet):
    queryset = CostTypeModel.objects.all()
    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized Attraction instance
        """
        new_costtype = CostTypeModel()
        new_costtype.name = request.data["name"]
        new_costtype.color = request.data["color"]
        serializer = CostTypeSerializer(new_costtype, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single park area
        Returns:
            Response -- JSON serialized park area instance
        """
        try:
            costtype = CollegeModel.objects.get(pk=pk)
            serializer = CostTypeSerializer(costtype, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single product are
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            costtype = CostTypeModel.objects.get(pk=pk)
            costtype.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except CostTypeModel.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to payment types resource

        Returns:
            Response -- JSON serialized list of payment types
        """
        costtypes = CostTypeModel.objects.all()
        name = self.request.query_params.get('name', None)
        color= self.request.query_params.get('color', None)

        serializer = CostTypeSerializer(
            costtypes, many=True, context={'request': request})
        return Response(serializer.data)

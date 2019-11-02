from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User
from collegecost_api.models import *

class YearSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = YearModel
        url = serializers.HyperlinkedIdentityField(
            view_name='year',
            lookup_field='id'
        )
        fields = ('id', 'name', 'college', 'year', 'yearly_cost', 'yearly_payment', 'yearly_balance')
        depth = 2

class YearSlimSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = YearModel
        url = serializers.HyperlinkedIdentityField(
            view_name='year',
            lookup_field='id'
        )
        fields = ('id', 'name', 'yearly_cost', 'yearly_payment', 'yearly_balance')

class Year(ViewSet):
    queryset = YearModel.objects.all()
    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized Attraction instance
        """
        new_year = YearModel()
        new_year.name = request.data["name"]
        new_year.year = request.data["year"]
        new_year.college = CollegeModel.objects.get(pk=request.data['college'])
        new_year.save()



        serializer = YearSerializer(new_year, context={'request': request})
        return Response(serializer.data)



    def retrieve(self, request, pk=None):
        """Handle GET requests for single park area
        Returns:
            Response -- JSON serialized park area instance
        """
        try:
            year = YearModel.objects.get(pk=pk)
            serializer = YearSerializer(year, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single product are
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            year = YearModel.objects.get(pk=pk)
            year.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except CollegeModel.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to payment types resource

        Returns:
            Response -- JSON serialized list of payment types
        """
        years = YearModel.objects.all()

        name = self.request.query_params.get('name', None)
        year = self.request.query_params.get('year', None)
        college = self.request.query_params.get('college', None)

        


        serializer = YearSerializer(
            years, many=True, context={'request': request})
        return Response(serializer.data)



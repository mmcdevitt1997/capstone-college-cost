from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User
from collegecost_api.views.costview import CostSerializer
from collegecost_api.views.paymentview import PaymentSerializer
from collegecost_api.models import *
from collegecost_api.views.helper import FlattenMixin

class YearSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = YearModel
        url = serializers.HyperlinkedIdentityField(
            view_name='year',
            lookup_field='id'
        )
        fields = ('id', 'name', 'college', 'year', 'cost', 'payment', 'yearly_balance', 'cost_color', 'payment_color')
        depth = 1

class YearSlimSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = YearModel
        url = serializers.HyperlinkedIdentityField(
            view_name='year',
            lookup_field='id'
        )
        fields = ('id', 'name', 'cost', 'payment', 'yearly_balance')

class YearChartDataSerializer(serializers.HyperlinkedModelSerializer):
    costs = CostSerializer(many="True")
    payments = PaymentSerializer(many="True")



    class Meta:
        model = YearModel
        url = serializers.HyperlinkedIdentityField(
            view_name='year',
            lookup_field='id'
        )

        fields = ('id', 'name', 'yearly_balance', 'year', 'payments', 'costs', 'cost', 'payment', 'cost_color','payment_color', 'college')



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
    def update(self, request, pk=None):
        """Handle PUT requests for a single payment type

        Returns:
            Response -- Empty body with 204 status code
        """

        update_year = YearModel.objects.get(pk=pk)
        update_year.name = request.data["name"]

        update_year.save()


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
        collegeId = self.request.query_params.get('collegeId', None)
        year_all = YearModel.objects.all()
        years = year_all.filter( college = collegeId)

        chartdata = self.request.query_params.get('chartdata', None)
        if chartdata is not None:
            for x in years:
                relatedcost = CostModel.objects.filter(year=x)
                x.costs = relatedcost
                relatedpayment = PaymentModel.objects.filter(year=x)
                x.payments = relatedpayment

            serializer = YearChartDataSerializer(
                years, many=True, context={'request': request})
            return Response(serializer.data)

        serializer = YearSerializer(
            years, many=True, context={'request': request})
        return Response(serializer.data)



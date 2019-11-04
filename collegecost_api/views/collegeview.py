"""View module for handling requests about colleges"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User
from collegecost_api.views.yearview import *
from collegecost_api.views.paymentview import PaymentSerializer
from collegecost_api.models import *

class CollegeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CollegeModel
        url = serializers.HyperlinkedIdentityField(
            view_name='college',
            lookup_field='id'
        )
        fields = ('id', 'user_id', 'numberofyears', 'name', 'college_total_payment', 'college_total_cost', 'college_balance')
        depth = 1
class CollegeDatatSerializer(serializers.HyperlinkedModelSerializer):
    years = YearSlimSerializer(many=True)

    class Meta:
        model = CollegeModel
        url = serializers.HyperlinkedIdentityField(
            view_name='college',
            lookup_field='id'
        )
        fields = ('id', 'name', 'years')
        depth = 1

class College(ViewSet):
    queryset = CollegeModel.objects.all()
    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serializes college instance
        """
        new_college = CollegeModel()
        new_college.name = request.data["name"]
        new_college.numberofyears = request.data["numberofyears"]
        user = request.auth.user
        new_college.user = user
        new_college.save()
        serializer = CollegeSerializer(new_college, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single college
        Returns:
            Response -- JSON serialized college instance
        """
        college = CollegeModel.objects.get(pk=pk)
        chartdata = self.request.query_params.get('chartdata', None)
        if chartdata is not None:
            relateddata = YearModel.objects.filter(college=pk)
            college.years = relateddata
            serializer = CollegeDatatSerializer(
                college, context={'request': request})
            return Response(serializer.data)

        serializer = CollegeSerializer(college, context={'request': request})
        return Response(serializer.data)
        
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single college
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            college = CollegeModel.objects.get(pk=pk)
            college.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except CollegeModel.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to all of the college  resource

        Returns:
            Response -- JSON serialized list of colleges
        """

        colleges = CollegeModel.objects.filter(user=request.auth.user)

        chartdata = self.request.query_params.get('chartdata', None)
        if chartdata is not None:
            for x in colleges:
                relateddata = YearModel.objects.filter(college=x)
                x.years = relateddata

            serializer = CollegeDatatSerializer(
                colleges, many=True, context={'request': request})
            return Response(serializer.data)

        serializer = CollegeSerializer(
            colleges, many=True, context={'request': request})
        return Response(serializer.data)

"""View module for handling requests about customers"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User
from collegecost_api.models import CollegeModel

class CollegeSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = CollegeModel
        url = serializers.HyperlinkedIdentityField(
            view_name='college',
            lookup_field='id'
        )
        fields = ('id', 'url', 'user', 'startdate', 'enddate')
        depth = 1

class College(ViewSet):
     def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized Attraction instance
        """
        new_college = CollegeModel()
        new_college.name = request.data["name"]
        new_college.startdate = request.data["startdate"]
        new_college.enddate = request.data["enddate"]



        serializer = CustomerSerializer(new_customer, context={'request': request})

        return Response(serializer.data)

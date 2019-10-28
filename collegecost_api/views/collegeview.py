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
        user = CollegeModel.objects.get(user=request.auth.user)
        new_college.user = user
        serializer = CollegeSerializer(new_college, context={'request': request})
        return Response(serializer.data)

def retrieve(self, request, pk=None):
    """Handle GET requests for single park area
    Returns:
        Response -- JSON serialized park area instance
    """
    try:
        college = CollegeModel.objects.get(pk=pk)
        serializer = CollegeSerializer(college, context={'request': request})
        return Response(serializer.data)
    except Exception as ex:
        return HttpResponseServerError(ex)

def destroy(self, request, pk=None):
    """Handle DELETE requests for a single product are
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


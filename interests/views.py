from django.shortcuts import render
from interests.models import Interest
from interests.serializers import InterestsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


class InterestList(APIView):
    """
    List all interests, or create a new interest.
    """
    #authentication_classes = [SessionAuthentication,BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        interests = Interest.objects.all()
        serializer = InterestsSerializer(interests, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InterestsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InterestDetail(APIView):
    """
    Retrieve, update or delete a Interest instance.
    """
    #authentication_classes = [SessionAuthentication,BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Interest.objects.get(pk=pk)
        except Interest.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        interest = self.get_object(pk)
        serializer = InterestsSerializer(interest)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        interest = self.get_object(pk)
        serializer = InterestsSerializer(interest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        interest = self.get_object(pk)
        interest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

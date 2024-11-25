from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import Request
from .serializers import RequestSerializer

class RequestView(APIView):
    def get(self, request):
        # Handle GET request: Retrieve all requestls
        request = Request.objects.all()
        serializer = RequestSerializer(request, many=True)
        return Response(serializer.data)
    def post(self, request):
        # Handle POST request: Add a new request
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from mainapp.calculate import *
from .serializers import ReviewSerializer, ShipSerializer
from .models import Review, Post,Ship
# Create your views here.

class ShipList(APIView):
    def get(self, request):
        ships= Ship.objects.all()

        serializer = ShipSerializer(ships, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShipSerializer(
            data = request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ShipDetail(APIView):
    def get_object(self, pk):
        try:
            return Ship.objects.get(pk=pk)

        except Ship.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        ship = self.get_object(pk)
        serializer = ShipSerializer(ship)
        return Response(serializer.data)

    def put(self, request, pk, format =None):
        ship = self.get_object(pk)
        serializer = ShipSerializer(ship, data = change_ship_attribute(request.data))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        ship = self.get_object(pk)
        ship.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class PostList(APIView):
    def get(self, request):
        reviews = Post.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

class ReviewList(APIView):
    def get(self, request):
        reviews= Review.objects.all()

        serializer = ReviewSerializer(reviews, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(
            data = request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ReviewDetail(APIView):
    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)

        except Review.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request, pk, format =None):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        review = self.get_object(pk)
        review.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
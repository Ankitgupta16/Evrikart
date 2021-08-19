from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import Http404

from .serializers import UrstoreSerializer
from .models import Urstore


# Views using APIView
class UrstoreList(APIView):

    serializer_class = UrstoreSerializer

    def get(self, request, pk=None, format=None):
        id=pk
        if id is not None:
            Urs = Urstore.objects.get(id=id)
            data = UrstoreSerializer(Urs, many=True).data
            return Response(data)

        Urs = Urstore.objects.all()
        data = UrstoreSerializer(Urs, many=True).data
        return Response(data)

    def post(self, request, format=None):
        serializer = UrstoreSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UrstoreView(APIView):


    serializer_class = UrstoreSerializer

    def get(self, request, pk=None, format=None):
        Urs = get_object_or_404(Urstore, pk=pk)
        try:
            serializer = UrstoreSerializer(Urs)
            data = serializer.data
        except:
            data = status.HTTP_400_BAD_REQUEST
        return Response(data)


    def put(self, request,pk,format=None):
        Urs = get_object_or_404(Urstore, pk=pk)
        serializer = UrstoreSerializer(Urs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request,pk, format=None):
        id=pk
        Urs = Urstore.objects.get(pk=id)
        serializer = UrstoreSerializer(Urs, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        store = get_object_or_404(Urstore, pk=pk)
        store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
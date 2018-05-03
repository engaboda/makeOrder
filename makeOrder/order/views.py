from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Order
from .serializers import OrderSerializers
from rest_framework.views import  Response

# Create your views here.
@api_view(['GET', 'POST'])
def order_list(request):
    """
    List all Orders, or create a new Order.
    """
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializers(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

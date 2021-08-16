from rest_framework.views import APIView
from .serializers import OrderSerializer, OrderItemSerializers, CouponSerializers
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem, Coupon
from rest_framework.permissions import IsAuthenticated
from permissions import IsOwnerOrReadOnly


#order

class OrderListView(APIView):
    def get(self, request):
        order = Order.objects.all()
        srz_data = OrderSerializer(instance=order, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)


class OrderCreateView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        data = OrderSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly, ]


    def put(self, request, pk):
        order = Order.objects.get(pk=pk)
        self.check_object_permissions(request, order)
        srz_data = OrderSerializer(instance=order, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDeleteView(APIView):
    permission_classes = [ IsOwnerOrReadOnly, ]

    def delete(self, request, pk):
        order = Order.objects.get(pk=pk)
        self.check_object_permissions(request, order)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# order item

class OrderItemListView(APIView):
    def get(self, request):
        orderitem = OrderItem.objects.all()
        srz_data = OrderItemSerializers(instance=orderitem, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)


class OrderItemCreateView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        data = OrderItemSerializers(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderItemUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly, ]

    def put(self, request, pk):
        orderitem = OrderItem.objects.get(pk=pk)
        self.check_object_permissions(request, orderitem)
        srz_data = OrderItemSerializers(instance=orderitem, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderItemDeleteView(APIView):
    permission_classes = [IsOwnerOrReadOnly, ]

    def delete(self, request, pk):
        orderitem = OrderItem.objects.get(pk=pk)
        self.check_object_permissions(request, orderitem)
        orderitem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)































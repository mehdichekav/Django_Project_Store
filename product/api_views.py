from rest_framework.views import APIView
from .serializers import ProductSerializer, CategorySerializers, DiscountSerializers
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category, Discount
from rest_framework.permissions import IsAuthenticated
from permissions import IsOwnerOrReadOnly


#order

class ProductListView(APIView):
    def get(self, request):
        product = Product.objects.all()
        srz_data = ProductSerializer(instance=product, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)


class ProductCreateView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        data = ProductSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly, ]


    def put(self, request, pk):
        product = Product.objects.get(pk=pk)
        self.check_object_permissions(request, product)
        srz_data = ProductSerializer(instance=product, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDeleteView(APIView):
    permission_classes = [ IsOwnerOrReadOnly, ]

    def delete(self, request, pk):
        product = Product.objects.get(pk=pk)
        self.check_object_permissions(request, product)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# order item

class CategoryListView(APIView):
    def get(self, request):
        category = Category.objects.all()
        srz_data = CategorySerializers(instance=category, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)


class CategoryCreateView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        data = CategorySerializers(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly, ]

    def put(self, request, pk):
        category = Category.objects.get(pk=pk)
        self.check_object_permissions(request, category)
        srz_data = CategorySerializers(instance=category, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDeleteView(APIView):
    permission_classes = [IsOwnerOrReadOnly, ]

    def delete(self, request, pk):
        category = Category.objects.get(pk=pk)
        self.check_object_permissions(request, category)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)































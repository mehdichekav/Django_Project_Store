from rest_framework.views import APIView
from .serializers import UserSerializer, AddressSerializers, ProfileSerializers
from rest_framework.response import Response
from rest_framework import status
from .models import User, Address, Profile
from rest_framework.permissions import IsAuthenticated
from permissions import IsOwnerOrReadOnly

#user
class UserListView(APIView):
    def get(self, request):
        user = User.objects.all()
        srz_data = UserSerializer(instance=user, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)


class UserCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = UserSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        self.check_object_permissions(request, user)
        srz_data = UserSerializer(instance=user, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDeleteView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Address
class AddressListView(APIView):
    def get(self, request):
        address = Address.objects.all()
        srz_data = UserSerializer(instance=address, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)


class AddressCreateView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        data = AddressSerializers(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


class AddressUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly, ]

    def put(self, request, pk):
        address = User.objects.get(pk=pk)
        self.check_object_permissions(request, address)
        srz_data = AddressSerializers(instance=address, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class AddressDeleteView(APIView):
    permission_classes = [IsOwnerOrReadOnly, ]

    def delete(self, request, pk):
        address = Address.objects.get(pk=pk)
        self.check_object_permissions(request, address)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)































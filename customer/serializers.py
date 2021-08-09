# from django.contrib.auth.models import User
# from rest_framework import serializers
#
# from customer.models import Address
#
#
# class UserBriefSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fildes = ['id', 'username', 'phone', 'firstname', 'lastname']
#
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         exclude = ['password']
#
#
# class AddressBriefSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Address
#         fildes = ['id', 'owner', 'city']
#
#
# class AddressSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Address
#         fildes = '__all__'
#
#
#
#

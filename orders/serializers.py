from rest_framework import serializers

from .models import Order, OrderItem, Coupon


class OrderSerializer(serializers.ModelSerializer):
    # owner = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_owner(self, obj):
        result = obj.owner.all()
        return OrderItemSerializers(instance=result).data


class OrderItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class CouponSerializers(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'


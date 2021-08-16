from rest_framework import serializers

from .models import Order, OrderItem, Coupon


class OrderSerializer(serializers.ModelSerializer):
    order = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_order(self, obj):
        result = obj.owner.all()
        return OrderItemSerializers(instance=result, many=True).data


class OrderItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class CouponSerializers(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'

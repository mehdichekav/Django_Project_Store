from rest_framework import serializers
from .models import Product, Category, Discount


class ProductSerializer(serializers.ModelSerializer):
    # product = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_product(self, obj):
        result = obj.owner.all()
        return CategorySerializers(instance=result, many=True).data


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DiscountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'


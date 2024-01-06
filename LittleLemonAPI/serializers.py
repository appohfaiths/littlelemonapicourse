from rest_framework import serializers
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
import bleach
from .models import MenuItem, Category, Cart, Order, OrderItem, Groups, UserProfile


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']


class MenuItemSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        attrs['title'] = bleach.clean(attrs['title'])
        if (attrs['price'] < 1):
            raise serializers.ValidationError("Price must not be less than 1")
        return super().validate(attrs)

    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price',
                  'featured', 'category', 'category_id']
        extra_kwargs = {
            'title': {
                'validators': [
                    UniqueValidator(queryset=MenuItem.objects.all())
                ]
            }
        }
        depth = 1


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'menuitem', 'quantity', 'unit_price', 'price']
        extra_kwargs = {
            'user': {
                'validators': [
                    UniqueValidator(queryset=Cart.objects.all())
                ]
            }
        }


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'delivery_crew', 'status', 'total', 'date']
        extra_kwargs = {
            'user': {
                'validators': [
                    UniqueValidator(queryset=Order.objects.all())
                ]
            }
        }


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'menuitem', 'quantity', 'unit_price', 'price']
        extra_kwargs = {
            'order': {
                'validators': [
                    UniqueValidator(queryset=OrderItem.objects.all())
                ]
            }
        }


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ['id', 'name']
        extra_kwargs = {
            'name': {
                'validators': [
                    UniqueValidator(queryset=Groups.objects.all())
                ]
            }
        }


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        extra_kwargs = {
            'user': {
                'validators': [
                    UniqueValidator(queryset=UserProfile.objects.all())
                ]
            }
        }
        depth = 1

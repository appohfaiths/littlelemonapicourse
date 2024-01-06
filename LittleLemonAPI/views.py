from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .models import MenuItem, Category, Cart, Order, OrderItem, UserProfile
from .serializers import MenuItemSerializer, CategorySerializer, CartSerializer, OrderSerializer, OrderItemSerializer, GroupSerializer, UserProfileSerializer

# Create your views here.


@api_view()
def index(request):
    return Response({"message": "Little Lemon API!"})

# Menu Views


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'category']
    search_fields = ['title', 'category']

    def get_permissions(self):
        if (self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']):
            return [IsAuthenticated()]
        return []

    def get_queryset(self):
        queryset = MenuItem.objects.all()

        perpage = self.request.query_params.get('perpage', default=10)
        page = self.request.query_params.get('page', default=1)

        paginator = Paginator(queryset, per_page=perpage)

        try:
            queryset = paginator.page(number=page)
        except EmptyPage:
            queryset = []
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"menu_items": serializer.data})


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if (self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']):
            return [IsAuthenticated()]
        return []

# Cart Views


class CartView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

# Order Views


class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = MenuItem.objects.all()

        perpage = self.request.query_params.get('perpage', default=10)
        page = self.request.query_params.get('page', default=1)

        paginator = Paginator(queryset, per_page=perpage)

        try:
            queryset = paginator.page(number=page)
        except EmptyPage:
            queryset = []
        return queryset


class OrderItemView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

# Manager Views


class ManagerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        queryset = UserProfile.objects.all()
        group_name = self.request.query_params.get('group_name', default=None)

        if group_name:
            queryset = queryset.filter(user__groups__name=group_name)

        perpage = self.request.query_params.get('perpage', default=10)
        page = self.request.query_params.get('page', default=1)

        paginator = Paginator(queryset, per_page=perpage)

        try:
            queryset = paginator.page(number=page)
        except EmptyPage:
            queryset = []
        return queryset

    def get_permissions(self):
        if (self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']):
            return [IsAuthenticated()]
        return []


class GroupUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        queryset = UserProfile.objects.all()
        group_name = self.request.query_params.get('group_name', default=None)

        if group_name:
            queryset = queryset.filter(user__groups__name=group_name)

        perpage = self.request.query_params.get('perpage', default=10)
        page = self.request.query_params.get('page', default=1)

        paginator = Paginator(queryset, per_page=perpage)

        try:
            queryset = paginator.page(number=page)
        except EmptyPage:
            queryset = []
        return queryset

    def get_permissions(self):
        if (self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']):
            return [IsAuthenticated()]
        return []

# Category views


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if (self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']):
            return [IsAuthenticated()]
        return []

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu-items', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('groups/<str:group_name>/users', views.GroupUserView.as_view()),
    path('groups/<str:group_name>/users/<int:pk>',
         views.GroupUserView.as_view()),
    path('cart/menu-items', views.CartView.as_view(),  name='cart'),
    path('orders', views.OrderView.as_view(), name='orders'),
    path('orders/<int:pk>', views.OrderView.as_view(), name='orders'),
    path('categories', views.CategoryView.as_view(), name='categories'),
]

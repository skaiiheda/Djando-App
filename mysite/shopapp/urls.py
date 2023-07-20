from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.views.decorators.cache import cache_page
from .views import (ShopIndexView,
                    # products_list,
                    ProductsListView,
                    # order_list,
                    # create_product,
                    # create_order,
                    GroupsListView,
                    ProductDetailsView,
                    ProductCreateView,
                    ProductUpdateView,
                    ProductDeleteView,
                    OrdersListView,
                    OrderDetailsView,
                    OrderCreateView,
                    OrderUpdateView,
                    OrderDeleteView,
                    ProductsDataExportView,
                    OrdersDataExportView,
                    ProductViewSet,
                    )

app_name = 'shopapp'

routers = DefaultRouter()
routers.register("products", ProductViewSet)

urlpatterns = [
    # path('', cache_page(60 * 3)(ShopIndexView.as_view()), name='index'),
    path('', ShopIndexView.as_view(), name='index'),
    path("api/", include(routers.urls)),
    path('groups/', GroupsListView.as_view(), name='groups_list'),
    path('products/export/', ProductsDataExportView.as_view(), name='products-export'),
    path('orders/export/', OrdersDataExportView.as_view(), name='orders-export'),
    path('products/', ProductsListView.as_view(), name='products_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    # path('products/create_another/', create_product, name='products_create'),
    path('products/<int:pk>/', ProductDetailsView.as_view(), name='product_details'),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/archive/', ProductDeleteView.as_view(), name='product_delete'),
    path('orders/', OrdersListView.as_view(), name='orders_list'),
    path('orders/create/', OrderCreateView.as_view(), name='order_create'),
    path('orders/<int:pk>/', OrderDetailsView.as_view(), name='order_details'),
    path('orders/<int:pk>/update', OrderUpdateView.as_view(), name='order_update'),
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),
]

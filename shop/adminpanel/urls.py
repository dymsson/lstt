from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='pages'),
    path('products/', products_list, name='show_product'),
    path('products/create/', product_create, name='create_product'),
    path('products/update/<int:id>', product_update, name='update_product'),
    path('products/delete/<int:id>', product_delete, name='delete_product'),

    path('categories', categories_list, name='show_category'),
    path('categories/create/', category_create, name='create_category'),
    path('categories/update/<int:id>', category_update, name='update_category'),
    path('categories/delete/<int:id>', category_delete, name='delete_category'),

    path('shops', shops_list, name='show_shop'),
    path('shops/create/', shop_create, name='create_shop'),
    path('shops/update/<int:id>', shop_update, name='update_shop'),
    path('shops/delete/<int:id>', shop_delete, name='delete_shop'),
]

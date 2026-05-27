from django.urls import path
from .views import add_product,view_all_products,delete_by_id,add_to_cart

urlpatterns=[
    path('add_product/', add_product),
    path('view_all_products/',view_all_products, name='view'),
    path('delete_by_id/<int:id>',delete_by_id),

    path('add_to_cart/<int:id>',
         add_to_cart,
         name='add_to_cart'),

]





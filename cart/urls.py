from django.urls import path
from . import views


urlpatterns = [
    path('cartdetails',views.cart_details,name='cartdetails'),
    path('add/<int:product_id>/',views.add_cart,name='addcart'),
    path('cart_dec/<int:product_id>/',views.min_cart,name='cart_dec'),
    path('remove/<int:product_id>/',views.cart_remove,name='remove'),
    path('payment',views.payment,name='payment'),
    path('success',views.success,name='success'),
    
]
from django.urls import path
from . import views


urlpatterns = [
    path('',views.mainpage,name='mainpage'),
    path('home',views.home,name='home'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>',views.proddetails,name='details'),
    
    
]
from django.urls import path
from . import views

urlpatterns = [
    path('c_home', views.home),
    path('c_cart', views.cart),
    path('c_prdt', views.product_details),
    path('c_myorders', views.my_orders),
    path('c_profile', views.profile),
    path('c_chge pswd', views.change_passwd),

]





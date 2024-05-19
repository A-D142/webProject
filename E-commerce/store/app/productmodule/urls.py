from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cart', views.cart, name='cart'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('addproduct', views.addproduct, name='addproduct'),
    path('updateproduct/<int:id>', views.updateproduct, name='updateproduct'),
    path('product/<int:id>', views.product, name='product'),
    path('update', views.update, name='update'),
    path('deletecart', views.deletecart, name='deletecart'),
]
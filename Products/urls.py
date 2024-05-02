from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.SignUp.as_view(), name='signUp'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('product-list/', views.GetProductList.as_view(), name='productlist'),
    path('product-search/', views.SearchProduct.as_view(), name= 'paroductsearch'),
]
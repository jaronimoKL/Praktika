from django.urls import path

from santehcom import views
from santehcom.views import *

urlpatterns = [
    path('search/', SearchListView.as_view(), name='search'),
    path('', Product, name='main'),
    path('catalog_list/', CatalogList, name='catalog-list'),
    path('product/<slug:slug>/', ProductDetail, name="product_detail"),
    path('catalog/', Catalog, name='catalog'),
    path('contact/', Contact, name='contact'),
    path('about/', About, name='about'),
    path('feedback/', Feedback, name='feedback'),
    path('develop/', Develop, name='develop'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser, name='logout'),
    path('profile/', ProfileUser, name='profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password-change'),
]

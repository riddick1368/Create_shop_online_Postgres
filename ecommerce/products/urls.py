from django.contrib import admin
from django.urls import path,include,re_path

from . import views
app_name="products"




urlpatterns = [
    path('productlist',views.ProductListView,name='productlist'),
    re_path(r'^(?P<id>\d+)/$',views.ProductDetailView,name="product_detail_view"),
    path('categorylist', views.CategoryListview, name='categorylistview'),
    re_path(r'^category/(?P<id>\d+)/$',views.CategoryDetail,name= "category_detail")

]
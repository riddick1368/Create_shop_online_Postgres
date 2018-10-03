from django.contrib import admin
from django.urls import path,include,re_path
from . import views


app_name = 'blog'



urlpatterns = [
    re_path(r'^post-list/$',views.PostList,name ='postlist'),
    re_path(r'^post-list/(?P<id>\d+)/$',views.PostDetail,name="postdetail"),
    path ('post-create',views.CreatPost, name='post-create'),
    re_path (r'^post-list/update/(?P<id>\d+)/$',views.PostUpdateis,name='update-post'),
    # re_path(r'^(?P<slug_post>[-\w])+/$',views.PostDetail,name="postdetail"),

]
from django.contrib import admin
from django.urls import path,include,re_path
from . import views


app_name = 'blog'



urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('post-list',views.PostList,name ='postlist'),
    re_path(r'^(?P<slug_post>[-\w])+/$',views.PostDetail,name="postdetail"),
    path ('post-create',views.CreatPost, name='post-create')
    ]
from django.contrib import admin
from django.urls import path,include,re_path
from . import views




app_name = 'accounts'



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.user_login,name= "login"),
    path('logout/',views.user_logout,name='logout'),
    path ('register/',views.register_user,name='register_user'),
    path('change-password/',views.Change_Password,name="change_password"),
    # re_path(r'(?P<username>[\w,@+-]+)/$',views.ViewProfile,name='viewprofile-with username'),
    # path('profile/',views.ViewProfile,name='viewprofile'),
    path('contact/',views.ContactUs,name='contact')

]
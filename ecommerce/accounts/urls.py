from django.contrib import admin
from django.urls import path,include
from . import views




app_name = 'accounts'



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.user_login,name= "login"),
    path('logout',views.user_logout,name='logout'),
    path ('register',views.register_user,name='register_user'),
    path('change-password',views.Change_Password,name="change_password")
    ]
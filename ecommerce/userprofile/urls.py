from django.contrib import admin
from django.urls import path,include




app_name ="userprofile"

urlpatterns = [
    path('admin/', admin.site.urls),
    ]
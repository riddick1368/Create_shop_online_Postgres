from django.contrib import admin
from .models import Post
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import UserProfile

# Register your models here.
class UserProfileInline(admin.StackedInline):
    model = UserProfile


class CustomUserInline(UserAdmin):
    inlines = (UserProfileInline,)




admin.site.register(Post)
admin.site.unregister(User)
admin.site.register(User,CustomUserInline)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Profile
from .models import Post
from .models import Service
# Register your models here.


admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Service)

class UserAdmin(admin.ModelAdmin):

    list_display=('username','email','is_staff')
    search_fields =('username','email','is_staff')
    list_per_page=25

admin.site.register(User, UserAdmin)
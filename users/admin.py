from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .forms import MakeUserForm, ChangeUserForm
from .models import User



class MyUserAdmin(UserAdmin):
    add_form = MakeUserForm
    form = ChangeUserForm
    model = User


admin.site.register(User, MyUserAdmin)
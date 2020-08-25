from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm


ADDITIONAL_USER_FIELDS = (
    (None, {'fields': ('age', 'bio', 'display_name', 'homepage')}),
)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = MyUser
    list_display = ['username','display_name', 'age', 'bio', 'homepage']

    add_fieldsets = UserAdmin.add_fieldsets + ADDITIONAL_USER_FIELDS
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_USER_FIELDS


    

    

admin.site.register(MyUser, CustomUserAdmin)
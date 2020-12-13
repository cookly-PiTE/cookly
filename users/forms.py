from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from .models import User


class MakeUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields


class ChangeUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields

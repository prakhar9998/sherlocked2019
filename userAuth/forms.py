from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Player

class CustomUserForm(UserCreationForm):
    zeal_Id = forms.CharField(max_length=200, required=True)

    # TODO: Add phone number, college name, and validation for phone no.
    class Meta(UserCreationForm.Meta):
        model = Player
        fields = ['username', 'password1', 'password2', 'zeal_Id', 'email', 'first_name', 'last_name']

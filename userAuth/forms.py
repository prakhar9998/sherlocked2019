from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Player

class CustomUserForm(UserCreationForm):
    zeal_Id = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Zeal ID'}),
        required=True)

    class Meta(UserCreationForm.Meta):
        model = Player
        fields = [
            'username',
            'password1',
            'password2',
            'zeal_Id',
            'email',
            'first_name',
            'last_name',
            'contact_no',
            'college_name',]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact No.'}),
            'college_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'College Name'})
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirmation'})

# class LoginForm(forms.ModelForm):

#     class Meta:
#         model = Player
#         fields = ['username', 'password',]
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'boom'})
#         }

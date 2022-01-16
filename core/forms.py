from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import UserProfile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Create a UserUpdateForm to update username and email
class UserUpdateForm(UserChangeForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def get_object(self):
        return self.request.user


#Update profile image
class ProfileImageUpdateForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']

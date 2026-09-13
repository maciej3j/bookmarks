from django.contrib.auth import get_user_model
from django.forms import CharField, Form, ModelForm, PasswordInput, ValidationError

from account.models import Profile


class LoginForm(Form):
    username = CharField()
    password = CharField(widget=PasswordInput)


class UserRegistrationForm(ModelForm):
    password = CharField(label="Password", widget=PasswordInput)
    password2 = CharField(label="Repeat password", widget=PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ("username", "first_name", "email")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise ValidationError("Passwords don't match.")
        return cd["password2"]


class UserEditForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email")


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ("date_of_birth", "photo")

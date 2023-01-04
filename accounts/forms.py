from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username", max_length=100, widget=forms.TextInput, required=True
    )
    password = forms.CharField(
        label="Password",
        max_length=100,
        widget=forms.PasswordInput,
        required=True,
        help_text="(case sensitive)",
    )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = "login"
        self.helper.add_input(Submit("submit", "Login"))


class RegisterForm(forms.Form):
    username = forms.CharField(
        label="Username", max_length=100, widget=forms.TextInput, required=True
    )
    password = forms.CharField(
        label="Password",
        max_length=100,
        widget=forms.PasswordInput,
        required=True,
        help_text="(case sensitive)",
    )
    password_confirm = forms.CharField(
        label="Password (again)",
        max_length=100,
        widget=forms.PasswordInput,
        required=True,
        help_text="(case sensitive)",
    )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = "register"
        self.helper.add_input(Submit("submit", "Register"))

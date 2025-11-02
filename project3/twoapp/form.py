from django import forms
from twoapp.models import User


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(
                attrs={"placeholder": "Enter your first name", "class": "form-control"}
            ),
            "last_name": forms.TextInput(
                attrs={"placeholder": "Enter your last name", "class": "form-control"}
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Enter your email address",
                    "class": "form-control",
                }
            ),
        }
        help_texts = {
            "first_name": "Enter your legal first name",
            "last_name": "Enter your legal last name",
            "email": "Enter a valid email address",
        }
        error_messages = {
            "first_name": {
                "required": "First name is required",
                "max_length": "First name must be less than %(limit_value)d characters",
            },
            "last_name": {
                "required": "Last name is required",
                "max_length": "Last name must be less than %(limit_value)d characters",
            },
            "email": {
                "required": "Email address is required",
                "invalid": "Please enter a valid email address",
            },
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if first_name and first_name.islower():
            self.add_error(
                "first_name", "First name should start with a capital letter"
            )

        if last_name and last_name.islower():
            self.add_error("last_name", "Last name should start with a capital letter")

        return cleaned_data

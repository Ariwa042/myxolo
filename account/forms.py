from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Deposit, Spend
from django.contrib.auth.forms import AuthenticationForm


# User registration form using Django's UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ('full_name', 'email', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already in use.")
        return username


# Form for deposit
class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ['amount']

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError("Amount must be greater than zero.")
        return amount


# Form for spending XP
class SpendForm(forms.ModelForm):
    class Meta:
        model = Spend
        fields = ['amount']

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError("Amount must be greater than zero.")
        return amount


class EmailAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(label='Email')

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        # Check if the email is associated with a user
        try:
            self.user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError('Invalid email or password.')

        # Authenticate using the email and password
        if not self.user.check_password(password):
            raise forms.ValidationError('Invalid email or password.')

        return self.cleaned_data
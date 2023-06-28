from django.contrib.auth.forms import UserCreationForm
from .models import Applicant


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Applicant
        fields = ('username', 'password1', 'password2', 'email')

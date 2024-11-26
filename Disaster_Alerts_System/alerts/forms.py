# alerts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import UserProfile
from .models import DisasterAlert

User = get_user_model()

class UserProfileCreationForm(UserCreationForm):
    # On n'ajoute plus first_name, last_name, ni birth_date ici
    address = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # Assurez-vous que le formulaire crée un UserProfile associé
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        profile = UserProfile.objects.create(user=user, address=self.cleaned_data['address'], phone_number=self.cleaned_data['phone_number'])
        return user

class DisasterAlertForm(forms.ModelForm):
    class Meta:
        model = DisasterAlert
        fields = ['type', 'location', 'severity', 'description']

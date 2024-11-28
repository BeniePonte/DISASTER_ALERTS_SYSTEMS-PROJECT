from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, DisasterAlert

# Define the choices for the location dropdown
LOCATION_CHOICES = [
    ('girne', 'Girne'),
    ('lefkoşa', 'Lefkoşa'),
    ('lefke', 'Lefke'),
    ('iskele', 'İskele'),
    ('gazimağusa', 'Gazimağusa'),
    ('güzelyurt', 'Güzelyurt'),
]

class UserProfileCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Enter a valid email address.")
    phone_number = forms.CharField(max_length=15, required=True, help_text="Enter your phone number.")
    location = forms.ChoiceField(choices=LOCATION_CHOICES, required=True, help_text="Select your location.")

    class Meta:
        model = UserProfile  # Use your custom user model
        fields = ['username', 'email', 'password1', 'password2', 'phone_number', 'location']

    def save(self, commit=True):
        # Save the user data to the UserProfile model
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        user.location = self.cleaned_data['location']
        if commit:
            user.save()
        return user

class DisasterAlertForm(forms.ModelForm):
    class Meta:
        model = DisasterAlert
        fields = ['type', 'location', 'severity', 'description']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'severity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 10}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

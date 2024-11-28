from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from rest_framework import viewsets
from .forms import UserProfileCreationForm, DisasterAlertForm
from .models import DisasterAlert
from .serializers import DisasterAlertSerializer
from django.contrib.auth.decorators import login_required

User = get_user_model()

def home(request):
    alerts = DisasterAlert.objects.all().order_by('-timestamp')
    return render(request, 'home.html', {'alerts': alerts})

def register(request):
    if request.method == 'POST':
        form = UserProfileCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Registration successful! You are now logged in.")
                return redirect('login')  # Redirect to the login page
            else:
                messages.error(request, "Registration failed. Please try again.")
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = UserProfileCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'registration/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def create_alert(request):
    # If the form is submitted via POST
    if request.method == 'POST':
        form = DisasterAlertForm(request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            form.save()  # Save the alert to the database
            messages.success(request, "Disaster alert created successfully!")  
            return redirect('home')  # Redirect to home page after alert creation
        else:
            # Display form validation errors
            messages.error(request, "Failed to create alert. Please correct the errors below.")
    
    else:
        form = DisasterAlertForm()  
    
    return render(request, 'create_alert.html', {'form': form})

@login_required
def update_alert(request, alert_id):
    alert = get_object_or_404(DisasterAlert, id=alert_id)

    if request.method == 'POST':
        form = DisasterAlertForm(request.POST, instance=alert)
        if form.is_valid():
            form.save()  
            return redirect('home')  # Redirect to the home page after successful update
        else:
            messages.error(request, "Failed to update alert. Please correct the errors below.")
    else:
        form = DisasterAlertForm(instance=alert)

    return render(request, 'edit_alert.html', {'form': form, 'alert': alert})

def list_alerts(request):
    alerts = DisasterAlert.objects.all().order_by('-timestamp')
    return render(request, 'list_alerts.html', {'alerts': alerts})



class DisasterAlertViewSet(viewsets.ModelViewSet):
    queryset = DisasterAlert.objects.all()
    serializer_class = DisasterAlertSerializer
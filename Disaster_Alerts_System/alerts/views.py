from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from rest_framework import viewsets
from .forms import UserProfileCreationForm, DisasterAlertForm
from .models import DisasterAlert
from .serializers import DisasterAlertSerializer

User = get_user_model()

# Home view
def home(request):
    alerts = DisasterAlert.objects.all().order_by('-timestamp')
    return render(request, 'home.html', {'alerts': alerts})

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserProfileCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            login(request, user)  # Log the user in immediately after registration
            messages.success(request, "Registration successful! Welcome.")
            return redirect('home')  # Redirect to the home page after successful registration
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = UserProfileCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to the homepage after successful login
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'registration/login.html')

# Logout view
def user_logout(request):
    logout(request)  # Log the user out
    return redirect('login')  # Redirect to the login page after logout

# Create alert view
def create_alert(request):
    if request.method == 'POST':
        alert_type = request.POST.get('type')  # Make sure this field is sent
        location = request.POST.get('location')
        severity = request.POST.get('severity')
        description = request.POST.get('description')

        if alert_type and location and severity:  # Ensure all required fields are provided
            try:
                DisasterAlert.objects.create(
                    type=alert_type,
                    location=location,
                    severity=int(severity),
                    description=description
                )
                messages.success(request, "Disaster alert created successfully!")
                return redirect('home')
            except Exception as e:
                messages.error(request, f"Failed to create alert: {e}")
        else:
            messages.error(request, "All fields except description are required.")
    return render(request, 'create_alert.html')

# Update alert view
def update_alert(request, alert_id):
    alert = get_object_or_404(DisasterAlert, id=alert_id)
    if request.method == 'POST':
        form = DisasterAlertForm(request.POST, instance=alert)
        if form.is_valid():
            form.save()
            messages.success(request, "Alert updated successfully!")
            return redirect('list_alerts')
    else:
        form = DisasterAlertForm(instance=alert)
    return render(request, 'alerts/update_alert.html', {'form': form})

# Alerts list view
def list_alerts(request):
    alerts = DisasterAlert.objects.all().order_by('-timestamp')  # Retrieve all alerts, sorted by date
    return render(request, 'list_alerts.html', {'alerts': alerts})

# Delete alert view
def delete_alert(request, alert_id):
    alert = get_object_or_404(DisasterAlert, id=alert_id)
    if request.method == 'POST':
        alert.delete()
        messages.success(request, "Alert deleted successfully!")
        return redirect('list_alerts')
    return render(request, 'alerts/confirm_delete.html', {'alert': alert})

# API ViewSet for Disaster Alerts
class DisasterAlertViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing disaster alerts.
    """
    queryset = DisasterAlert.objects.all()
    serializer_class = DisasterAlertSerializer

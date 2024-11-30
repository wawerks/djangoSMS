from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ScoreForm
from django.contrib.auth.forms import AuthenticationForm

@login_required
def score_view(request):
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            form.save()  # This will trigger the save method in the model
            return redirect('success_view')  # Redirect to a separate success view
    else:
        form = ScoreForm()
    return render(request, 'score_form.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():  # This checks if the form fields are populated and valid
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect('score_view')  # Redirect after successful login
            else:
                messages.error(request, "Invalid username or password.")  # Custom error message
        else:
            # Handle validation errors from the AuthenticationForm
            if form.has_error('username'):
                messages.error(request, "Username is invalid or missing.")
            if form.has_error('password'):
                messages.error(request, "Password is invalid or missing.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import SignupForm

def login(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup_success')  # Redirect to a success page
        # If form is not valid, render the form with errors
    else:
        form = SignupForm()
    return render(request, "login.html", {"form": form})


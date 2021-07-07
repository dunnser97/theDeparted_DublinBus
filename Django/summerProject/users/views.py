from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm
def register(request):
    """View to load the login page of our application and pass the built in django form to it"""
    # Check if the request received was posted as that would mean it's a form submission so the form should be created with the data received
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        # save the new user in the database if the form is valid
        if form.is_valid():
            form.save()
            print("user saved")
            # Redirect back to homepage after user is created
            return redirect("/")
    # If form was not posted then nothing was submitted by user so just load an empty form
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {"form": form})
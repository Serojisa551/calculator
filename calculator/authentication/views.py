from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.template import loader

# It is not working correctly yet TODO (
def authentication(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "authentication/authentication.html", {"form": form}) 
#)

def register(request):
    template = loader.get_template("authentication/registration.html")
    return HttpResponse(template.render())




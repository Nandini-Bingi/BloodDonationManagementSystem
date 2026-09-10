from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import DonorForm

# Create your views here.


def home(request):
    return render(request, 'home.html')

# def learn_more(request):
#     return render(request, "includes/about.html")

def contact(request):
    return render(request, "includes/navbar.html")

def register_donor(request):

    if request.method == "POST":

        form = DonorForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                messages.success(
                request,
                "🎉 Donor details submitted successfully!"
                )
                return redirect("register_donor")
            except:
                messages.error(
                    request,
                    "❌ Details not submitted. Please try again."
                )
        else:

            messages.error(
                request,
                "❌ Please correct the errors below."
            )

    else:
        form = DonorForm()

    return render(request, "register.html", {
        "form": form
    })
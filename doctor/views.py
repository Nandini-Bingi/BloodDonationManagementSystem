# from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DoctorLoginForm
from .models import Doctor
from donor.models import Donor
from django.db.models import Q

from django.utils import timezone

from datetime import date
from dateutil.relativedelta import relativedelta

from django.shortcuts import render, redirect, get_object_or_404
# from donor.models import Donor


def doctor_login(request):

    if request.method == "POST":

        form = DoctorLoginForm(request.POST)

        if form.is_valid():

            doctor_id = form.cleaned_data["doctor_id"]
            password = form.cleaned_data["password"]

            try:

                doctor = Doctor.objects.get(
                    doctor_id=doctor_id,
                    password=password
                )

                request.session["doctor_id"] = doctor.id

                return redirect("doctor_dashboard")

            except Doctor.DoesNotExist:

                messages.error(
                    request,
                    "Invalid Doctor ID or Password."
                )

    else:

        form = DoctorLoginForm()

    return render(
        request,
        "doctor_login.html",
        {"form": form}
    )


def doctor_dashboard(request):

    today = timezone.now().date()

    total_donors = Donor.objects.count()

    eligible_today = Donor.objects.filter(
    Q(next_eligible_date__isnull=True) |
    Q(next_eligible_date__lte=today)
    ).count() 

    donated_today = Donor.objects.filter(
        last_donation_date=today
    ).count()

    not_eligible = Donor.objects.filter(
        next_eligible_date__gt=today
    ).count()

    context = {

        "total_donors": total_donors,

        "eligible_today": eligible_today,

        "donated_today": donated_today,

        "not_eligible": not_eligible,

    }

    return render(
        request,
        "doctor_dashboard.html",
        context
    )



def search_donor(request):
    donor = None
    today = date.today()

    if request.method == "GET":
        query = request.GET.get("query")

        if query:
            donor = Donor.objects.filter(
                Q(aadhaar_number=query) |
                Q(phone_number=query)
            ).first()

    return render(
        request,
        "search_donor.html",
        {
            "donor": donor,
            "today": today
        }
    )


def total_donors(request):

    donors = Donor.objects.all().order_by("-id")

    return render(
        request,
        "total_donors.html",
        {
            "donors": donors
        }
    )


def eligible_today(request):
    today = date.today()

    donors = Donor.objects.filter(
        Q(next_eligible_date__isnull=True) |
        Q(next_eligible_date__lte=today)
    ).order_by("-id")

    return render(
        request,
        "eligible_today.html",
        {
            "donors": donors,
            "today": today
        }
    )


def donated_today(request):
    today = date.today()

    donors = Donor.objects.filter(
        last_donation_date=today
    ).order_by("-id")

    return render(
        request,
        "donated_today.html",
        {
            "donors": donors,
            "today": today
        }
    )


def not_eligible(request):
    today = date.today()

    donors = Donor.objects.filter(
        next_eligible_date__gt=today
    ).order_by("-id")

    return render(
        request,
        "not_eligible.html",
        {
            "donors": donors,
            "today": today
        }
    )


def donor_details(request, donor_id):

    donor = get_object_or_404(Donor, id=donor_id)

    return render(
        request,
        "donor_details.html",
        {
            "donor": donor,
            "today": date.today()
        }
    )


def update_donation(request, donor_id):

    donor = get_object_or_404(Donor, id=donor_id)

    today = date.today()

    # Check whether donor is already eligible
    if donor.next_eligible_date and donor.next_eligible_date > today:

        return render(
            request,
            "donor_details.html",
            {
                "donor": donor,
                "error": "This donor is not eligible to donate yet."
            }
        )

    if request.method == "POST":

        donor.last_donation_date = today

        donor.next_eligible_date = (
            today + relativedelta(months=3)
        )

        donor.save()

        return render(
            request,
            "donor_details.html",
            {
                "donor": donor,
                "success": "Donation details updated successfully."
            }
        )

    return redirect("donor_details", donor_id=donor.id)
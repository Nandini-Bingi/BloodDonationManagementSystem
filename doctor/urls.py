from django.urls import path
from . import views

urlpatterns = [

    path(
        "login/",
        views.doctor_login,
        name="doctor_login"
    ),

    path(
        "dashboard/",
        views.doctor_dashboard,
        name="doctor_dashboard"
    ),
    path(
        "search/",
        views.search_donor,
        name="search_donor"
    ),
    path(
    "total-donors/",
    views.total_donors,
    name="total_donors"
    ),
    path("eligible-today/", views.eligible_today, name="eligible_today"),
    path("donated-today/", views.donated_today, name="donated_today"),
    path("not-eligible/", views.not_eligible, name="not_eligible"),
    path(
    "donor/<int:donor_id>/",
    views.donor_details,
    name="donor_details"
    ),
    path(
    "donor/<int:donor_id>/update-donation/",
    views.update_donation,
    name="update_donation"
    ),
]
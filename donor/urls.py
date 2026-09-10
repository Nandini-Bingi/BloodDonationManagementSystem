from django.urls import path
from . import views

urlpatterns = [
    # path("learn-more/", views.learn_more, name="learn_more"),
    path("contact/", views.contact, name="contact"),

    path(
        "register/",
        views.register_donor,
        name="register_donor"
    ),
    

]
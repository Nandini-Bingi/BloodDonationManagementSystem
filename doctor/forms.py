from django import forms


class DoctorLoginForm(forms.Form):

    doctor_id = forms.CharField(
        max_length=20
    )

    password = forms.CharField(
        widget=forms.PasswordInput
    )
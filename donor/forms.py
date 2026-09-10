from django import forms
from .models import Donor
import re


class DonorForm(forms.ModelForm):

    class Meta:
        model = Donor

        fields = [
            'full_name',
            'phone_number',
            'aadhaar_number',
            'age',
            'gender',
            'blood_group',
            'address',
        ]

        widgets = {

            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Full Name'
            }),

            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '10-digit Phone Number'
            }),

            'aadhaar_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '12-digit Aadhaar Number'
            }),

            'age': forms.Select(
                choices=[(i, i) for i in range(18, 101)],
                attrs={'class': 'form-control'}
            ),

            'gender': forms.RadioSelect(),

            'blood_group': forms.Select(attrs={
                'class': 'form-control'
            }),

            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter Address'
            }),

        }

    def clean_phone_number(self):

        phone = self.cleaned_data['phone_number']

        if not re.fullmatch(r'\d{10}', phone):
            raise forms.ValidationError(
                "Phone number must contain exactly 10 digits."
            )

        return phone

    def clean_aadhaar_number(self):

        aadhaar = self.cleaned_data['aadhaar_number']

        if not re.fullmatch(r'\d{12}', aadhaar):
            raise forms.ValidationError(
                "Aadhaar number must contain exactly 12 digits."
            )

        return aadhaar
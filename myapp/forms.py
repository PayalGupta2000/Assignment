from django import forms

class VerificationForm(forms.Form):
    token = forms.CharField(max_length=100)

from django import forms


class SmsForm(forms.Form):
    receptor = forms.CharField(max_length=20)
    message = forms.CharField(max_length=500)

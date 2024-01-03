from django import forms


class LinkForm(forms.Form):
    original_link = forms.CharField(max_length=5000)

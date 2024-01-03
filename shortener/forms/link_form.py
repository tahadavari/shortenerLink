from django import forms
from django.core.validators import RegexValidator

url_validator = RegexValidator(
    regex=r'^(ftp|http|https):\/\/[^ "]+$',
    message='Enter a valid URL.',
)


class LinkForm(forms.Form):
    original_link = forms.CharField(max_length=5000, validators=[url_validator])

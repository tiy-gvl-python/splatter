
from django import forms
from django.forms import HiddenInput
from splat.models import Splat


# dead code
class SplatForm(forms.ModelForm):
    splatee = forms.CharField(widget=HiddenInput)

    class Meta:
        fields = ("message", "painting", "splatee")
        model = Splat
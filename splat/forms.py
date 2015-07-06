
from django import forms
from splat.models import Splat


class SplatForm(forms.ModelForm):

    def clean_splatee(self):
        print("we are in here")
        return self.cleaned_data['splatee']

    class Meta:
        exclude = ("splatee",)
        model = Splat
from django import forms
from django.contrib.auth.models import User
from .models import Event


class UserCodeForm(forms.Form):
    code = forms.CharField(
        label="Enter Event join code",
        max_length=120
    )

    # class Meta:
    #     model = User

    def clean_code(self):
        data = self.cleaned_data.get('code')

        if self.code != Event.ecode:
            raise forms.ValidationError('Code does not match')

        return data

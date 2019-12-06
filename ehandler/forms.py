from django import forms
from django.contrib.auth.models import User
from .models import Event, EventAttendance
# CODE FOR VERIFICATION OF EVENT CODE (LOGIC NOT WORKING WHY??)


# class CodeCheckForm(forms.Form):
#     event_code = forms.CharField(label='Enter event code', max_length=120)

#     def clean(self):
#         cleaned_data = super(CodeCheckForm, self).clean()
#         event_code = cleaned_data.get("event_code")
#         #p = Event.objects.values_list('ecode', flat=True)
#         try:
#             p = Event.objects.filter(ecode=event_code)
#         except Event.DoesNotExist:
#             raise forms.ValidationError("Enter valid code")


class CodeCheckForm(forms.ModelForm):
    ecode = forms.CharField(required=True)

    class Meta:
        model = Event
        fields = ['ecode']

    def clean_ecode(self, *args, **kwargs):
        ecode = self.cleaned_data.get("ecode")
        # event = Event.objects.get(pk=self.kwargs.get('pk'))
        # if ecode != event.ecode:
        #     raise forms.ValidationError("Enter the correct code")
        return ecode

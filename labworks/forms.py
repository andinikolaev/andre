from django import forms
from .models import Lab



class LabForm(forms.ModelForm):
    class Meta:
        model = Lab
        fields = ('name', 'comment', 'file')


def __init__(self, *args, **kwargs):
    super(LabForm, self).__init__(*args, **kwargs)
    self.fields['file'].required = False
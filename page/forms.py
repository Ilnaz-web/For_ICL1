from django import forms
from .models import *

class FilesForm(forms.ModelForm):

    class Meta:
        model = Files
        exclude = [""]
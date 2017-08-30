from django.db import models
from django.forms import ModelForm

class Files(models.Model):
    name = models.CharField(max_length=80)
    file = models.FileField(upload_to='excel_files')


class LoadForm(ModelForm):
        class Meta:
            model = Files
            fields = ['name', 'file']

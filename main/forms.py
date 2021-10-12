
from django import forms
from .models import Resume

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [ 'file']
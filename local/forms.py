from django import forms
from .models import entrydetails

class OriginalFeaturesForm(forms.ModelForm):
    class Meta:
        model = entrydetails
        fields = ['original_features']

from django import forms
from .models import Incident

class IncidentCreationForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['description', 'priority']

class IncidentUpdateForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['description', 'priority', 'status']

class IncidentSearchForm(forms.Form):
    search_query = forms.CharField(label='Search using Incident ID', max_length=20, required=False)

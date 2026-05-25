from django import forms
from .models import Content, Campaign, Platform

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'body', 'campaign', 'platform', 'scheduled_at']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'body': forms.Textarea(attrs={'class': 'w-full border rounded px-3 py-2', 'rows': 6}),
            'campaign': forms.Select(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'platform': forms.Select(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'scheduled_at': forms.DateTimeInput(attrs={'class': 'w-full border rounded px-3 py-2', 'type': 'datetime-local'}),
        }

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['name', 'description', 'platforms', 'start_date', 'end_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'description': forms.Textarea(attrs={'class': 'w-full border rounded px-3 py-2', 'rows': 4}),
            'platforms': forms.CheckboxSelectMultiple(),
            'start_date': forms.DateInput(attrs={'class': 'w-full border rounded px-3 py-2', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'w-full border rounded px-3 py-2', 'type': 'date'}),
        }
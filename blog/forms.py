"""Form for creating comments on the website"""
from django import forms
from .models import Experience


class ExperienceForm(forms.ModelForm):
    """Experience input form"""
    class Meta:
        "Metadata about form"
        model = Experience
        fields = ['pet_name', 'size', 'body', ]
        labels = {
            'pet_name': "Write your pet's name:",
            'size': 'Approximate size of your pet:',
            'body': 'Tell us about your pet here:',
        }
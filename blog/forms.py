"""Form for creating comments on the website"""
from django import forms
from .models import Comment

class ExperienceForm(forms.ModelForm):
    """Experience input form"""
    class Meta:
        "Metadata about form"
        model = Experience
        fields = ('pet_name', 'size','body',)
        labels = {
            'pet_name': "Write your pet's name"
            'size': 'What is approximate size oy your pet?'
            'body': 'Share your experience about your pet here.'
        }

class EditForm(forms.ModelForm):
    """Experience input form"""
    class Meta:
        "Metadata about form"
        model = Experience
        fields = ('pet_name', 'size','body',)
        labels = {
            'pet_name': "Correct name"
            'size': 'Correct size'
            'body': 'Make your changes below and click save.'
        }
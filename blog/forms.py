"""Form for creating comments on the website"""
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """Comment input form"""
    class Meta:
        "Metadata about form"
        model = Comment
        fields = ('is_question','body',)
        labels = {
            'body': ''
        }
        widgets = {
            'is_question' = forms.CheckboxInput(attrs={
                'class': 'custom-checkbox'}),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Share your experience or ask a question',
                'rows': '4',
                'cols': '40'}),
        }
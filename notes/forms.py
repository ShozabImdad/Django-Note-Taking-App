from django import forms
from .models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-3'}),
            'text': forms.Textarea(attrs={'class': 'form-control my-3'}),
        }
        labels = {
            'title': 'Title of Note',
            'text': "Write Your Note Here",
        }
        
   # def clean_title(self):
    #    title = self.cleaned_data['title']
    #    if 'django' not in title:
     #       raise forms.ValidationError('We Only Accepy Django Notes')
      #  return title
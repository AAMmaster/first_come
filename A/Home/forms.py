from django import forms
from .models import Resipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Resipe
        fields = ['title', 'description', 'image']
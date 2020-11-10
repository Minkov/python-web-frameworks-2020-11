from django import forms

from resources.models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'

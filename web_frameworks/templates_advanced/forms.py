from django import forms

from templates_advanced.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'class': 'my-textarea',
                },
            )
        }

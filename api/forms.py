from django import forms
from .models import Medicine

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'
        widgets = {
                    'med_n': forms.TextInput(attrs={'class': 'form-control'}),
                    'dose': forms.NumberInput(attrs={'class': 'form-control'}),
                    'price': forms.NumberInput(attrs={'class': 'form-control'}),
                    'until': forms.DateInput(attrs={'class': 'form-control'}),
                    'dev': forms.TextInput(attrs={'class': 'form-control'}),
                    'effect': forms.TextInput(attrs={'class': 'form-control'}),
                    'others': forms.TextInput(attrs={'class': 'form-control'}),
                    'amount': forms.NumberInput(attrs={'class': 'form-control'}),
                }
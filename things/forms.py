"""Forms of the project."""

from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Thing
# Create your forms here.

class ThingForm(forms.ModelForm):
    name = forms.CharField(label="Name",max_length=35)
    description =forms.CharField(label="Description",max_length=120)
    quantity = forms.IntegerField(label ="Quantity",validators=[MinValueValidator(0),MaxValueValidator(50)])


    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']

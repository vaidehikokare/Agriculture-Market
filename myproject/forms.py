from django import forms
from .models import Crop

class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ['crop_name', 'crop_type', 'quantity', 'price', 'contact_name', 'contact_email', 'contact_phone', 'description', 'photo', 'state', 'district', 'street_address']

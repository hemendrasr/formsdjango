from django import forms
from .models import Userdata
from django.core.exceptions import ValidationError
import re
class Userdataform(forms.ModelForm):
    class Meta:
        model=Userdata
        fields=['name','email','phno','gender','staddress','city','state','zipcode']
    gender_choices=[
        ('M','Male'),
        ('F','Female'),
        ('O','Others')  
    ]
    gender=forms.ChoiceField(choices=gender_choices,widget=forms.Select())
    state_choices=[
        ('RJ','Rajasthan'),
        ('PB','Punjab'),
        ('HR','Haryana'),
        ('MP','Madhya Pradesh')
    ]
    state=forms.ChoiceField(choices=state_choices,widget=forms.Select())
    def clean_phone(self):
        phno = self.cleaned_data.get('phone')
        if not re.match(r'^\+?1?\d{10}$', phno):
            raise ValidationError("Invalid phone number")
        return phno
    def clean_zipcode(self):
        zipcode = self.cleaned_data.get('zipcode')
        if not re.match(r'^\d{6}$', zipcode):  
            raise ValidationError("Invalid zipcode")
        return zipcode
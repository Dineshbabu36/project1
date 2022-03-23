from django import forms
from  .models import RegisterForm

class myRegisterForm(forms.ModelForm):
    class Meta:
        model=RegisterForm
        fields=["name","age","address","contact","email"]
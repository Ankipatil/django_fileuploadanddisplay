from django import forms
from .models import company

class companyform(forms.ModelForm):
    class Meta:
        model =  company
        fields = ('name','age','files')
    

    name = forms.CharField(widget=forms.TextInput({"placeholder":"Enter name"}))
    age = forms.IntegerField(widget=forms.TextInput({"placeholder":"Enter age"}))
    files = forms.FileField(widget=forms.FileInput({"placeholder":"enter file"}))
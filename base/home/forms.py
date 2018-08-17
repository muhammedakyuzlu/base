from django import forms



class User_input(forms.Form):
    name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'} ))
    date = forms.CharField(required=True,widget=forms.TextInput( attrs={'class':'form-control'} ))
    description=forms.CharField(required = True, widget = forms.TextInput(attrs={'class': 'form-control'}))

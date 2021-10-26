from django import forms
from django.forms.widgets import Widget
from .models import Pizza
from django import forms
from django.core.exceptions import ValidationError

class PizzaForm(forms.ModelForm):
    topping1 = forms.CharField(max_length=20,label='Topping 1:',
    widget=forms.TextInput(attrs={'class':'form-control'}))

    topping2 = forms.CharField(max_length=20,label='Topping 2:',
    widget=forms.TextInput(attrs={'class':'form-control'}))

 

    class Meta:
        model = Pizza
        fields = ['topping1','topping2','size']
        # labels = {'topping1':'Topping 1' , 'size':'Size'}

    def clean_topping1(self):
        cleaned_data = super().clean()
        top = cleaned_data['topping1']
        if len(top)<4:
            raise ValidationError("comeon worng!!")
        else:
            return top

class MultiplePizzaFrom(forms.Form):
    number = forms.IntegerField(min_value=2 , max_value=6)
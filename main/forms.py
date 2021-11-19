from django import forms
from .models import  jobCardsClass
from django.forms import ModelForm



class jobCardForm(forms.ModelForm):
    class Meta:
        model = jobCardsClass
        fields = '__all__'
        widgets = {
                    'dateRecieved': forms.SelectDateWidget,
                    'dateToBeCompleted' : forms.SelectDateWidget(),
                    'timeStarted': forms.TimeInput(attrs={'type': 'time'}),
                    'timeCompleted': forms.TimeInput(attrs={'type': 'time'}),
        }
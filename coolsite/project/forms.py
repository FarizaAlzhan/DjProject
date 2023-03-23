from django import forms
from .models import *

class AddTraining1Form(forms.ModelForm):
    title = forms.CharField(max_length=255, label="Название")
    time = forms.CharField(max_length=255, label="Время")
    place = forms.CharField(max_length=255, label="Место")
    training_manager = forms.CharField(max_length=255, label="Спикер")
    class Meta:
        model = Training1
        fields = ['title','time','place','training_manager','photo']



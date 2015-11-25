from django import forms
from core.models import *
from django.forms import ModelForm

class FormCoord(ModelForm):
    class Meta:
        model = Hueco
        fields = '__all__'

class FormRobo(ModelForm):
    class Meta:
        model = Robo
        fields = '__all__'

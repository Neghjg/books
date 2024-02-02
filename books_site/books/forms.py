from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class Comment(forms.ModelForm):
    CHOICES = [('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5')]
    rating = forms.ChoiceField(choices=(('1', "1"), ('2', "2"), ('3', "3"), ('4', "4"), ('5', "5")))
    comment = forms.CharField( widget=forms.Textarea(attrs={"class": "form-control", "placeholder" :"Комментарий"}))
    
    
    class Meta:
        model = Reviews
        fields = [ "rating", "comment"]
    

    
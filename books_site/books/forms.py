from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class Comment(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    CHOICES = [('1','1'),('2','2'), ('3','3'),('4','4'), ('5', '5')]
    #CHOICES = zip([1,2,3, 4, 5], ['1','2','3', '4', '5'])
    rating = forms.IntegerField(max_value = 5, widget=forms.RadioSelect(choices=CHOICES, attrs={"id": "rating-input"}))
    #rating = forms.ChoiceField(choices=((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")))
    comment = forms.CharField( widget=forms.Textarea(attrs={"class": "form-control", "placeholder" :"Комментарий"}))
    
    
    #parent_comment = forms.IntegerField(widget=forms.HiddenInput, required=False)
    class Meta:
        model = Reviews
        fields = [ "rating", "comment"]
    #    widgets ={
    #        "rating": forms.IntegerField(attrs={"class": "form_label"}),
    #        "comment": forms.CharField(attrs={"class": "form_label"})
    #    }
    #user = forms.CharField()
    #rating = forms.IntegerField(max_value= 5)
    #comment = forms.CharFiel d(label="", widget=forms.Textarea)
    

    
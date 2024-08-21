from django import forms
from postapp.models import PostModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets

class PostForm(forms.ModelForm):
    class Meta:
        model=PostModel
        fields=['text','photo']
        widgets={
        "text":forms.Textarea(attrs={"class":"form-control"})
         }
    


class SignUpForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','password'] 

    
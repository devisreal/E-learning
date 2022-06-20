from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserForm(forms.ModelForm):
   email = forms.EmailField()
   class Meta:
      model = User
      fields = ('username', 'first_name', 'last_name', 'email')
      labels = {
         'username': 'Username',
         'email': 'Email',
      }
   
   def __init__(self, *args: Any, **kwargs: Any) -> None:
      super(UserForm , self).__init__(*args, **kwargs)

      for fieldname in ('username', 'first_name', 'last_name', 'email'):
         self.fields[fieldname].help_text = None

class ProfileForm(forms.ModelForm):
   bio = forms.CharField(
      widget=forms.Textarea(
         attrs={
            'required': 'False',
            'placeholder': 'Tell us about yourself...',
         },         
      )
   )
   teacher = 'teacher',
   student = 'student',
   parent = 'parent',

   user_types = [
      ('teacher', 'teacher'),
      ('student', 'student'),
      ('parent', 'parent'),
   ]

   user_type = forms.ChoiceField(choices=user_types, required=True)

   class Meta:
      model = Profile
      fields = ('bio', 'profile_image', 'user_type')
      
from dataclasses import field
from django.forms import ModelForm
from .models import Submission, User,Course
from django.contrib.auth.forms import UserCreationForm


class SubmissionForm(ModelForm):
     class Meta:
        model = Submission
        fields =['details','Document']


class CustomUserCreationForum(UserCreationForm):
   class Meta:
      model = User
      fields = ['username', 'email', 'name','password1', 'password2']

from django import forms
from users.models import User

class EnrollmentForm(forms.Form):
      #  user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label=None)
      pass
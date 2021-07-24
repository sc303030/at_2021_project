from django import forms
from .models import *

class AuthorForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = "__all__"
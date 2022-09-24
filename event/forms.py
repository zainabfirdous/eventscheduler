from dataclasses import fields
from django import forms

from .models import Events

class Event(forms.ModelForm):
    class Meta:
        model = Events
        fields = "__all__"
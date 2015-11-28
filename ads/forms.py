from django import forms
from django.forms import fields, models, formsets, widgets
from django.forms import BaseFormSet, formset_factory, BaseInlineFormSet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import formset_factory
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core import validators
from django.contrib import messages

from .models import *


class AddItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ['photo','category', 'location', 'name', 'description', 'unit_cost', 'quantity']

	def __init__(self, *args, **kwargs):
		super(AddItemForm, self).__init__(*args, **kwargs)
		self.fields['category'].widget.attrs['class'] = 'form-control'
		self.fields['location'].widget.attrs['class'] = 'form-control'
		self.fields['photo'].widget.attrs['class'] = 'form-control'
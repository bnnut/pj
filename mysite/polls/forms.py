# -*- coding: utf-8 -*-
from django import forms

from .models import Crayfish


class Crayfishform(forms.ModelForm):

    class Meta:
        model = Crayfish
        fields = ('size', 'price')


class Crayfishform2(forms.ModelForm):

    class Meta:
        model = Crayfish
        fields = ('size',)
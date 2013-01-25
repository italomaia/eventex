# coding:utf-8

from django import forms
from django.utils.translation import gettext as _

class SubscriptionForm(forms.Form):
    name = forms.CharField(label=_('name'))
    cpf = forms.CharField(label=_('cpf'))
    email = forms.EmailField(label=_('email'))
    phone = forms.CharField(label=_('phone'))
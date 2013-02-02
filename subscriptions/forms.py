# coding:utf-8

from django import forms
from django.utils.translation import gettext as _

from subscriptions.models import Subscription

class SubscriptionForm(forms.ModelForm):
    name = forms.CharField(label=_('name'))
    cpf = forms.CharField(label=_('cpf'))
    email = forms.EmailField(label=_('email'))
    phone = forms.CharField(label=_('phone'))

    class Meta:
        model = Subscription
        exclude = ('paid',)
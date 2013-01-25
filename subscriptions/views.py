# coding:utf-8

from django.shortcuts import render

from forms import SubscriptionForm

def subscribe(request):
    form = SubscriptionForm()
    return render(request, 'subscriptions/subscription_form.html', {'form': form})

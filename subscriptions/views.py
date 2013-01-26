# coding:utf-8

from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404 as get_object

from models import Subscription
from forms import SubscriptionForm

def subscribe(request):
    form = SubscriptionForm(request.method == 'POST' and request.POST or None)
    if form.is_bound and form.is_valid():
        instance = form.save()
        return redirect(instance)
    return render(request, 'subscriptions/subscription_form.html',
        {'form': form})

def subscription(request, pk):
    instance = get_object(Subscription, pk=pk)
    return render(request, 'subscriptions/subscription_detail.html',
        {'subscriptions': instance})
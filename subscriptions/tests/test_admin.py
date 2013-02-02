# coding:utf-8

from django.test import TestCase

from mock import Mock
from subscriptions.models import Subscription


class MarkAsPaidTest(TestCase):
    def setUp(self):
        from subscriptions.admin import SubscriptionAdmin, admin

        self.model_admin = SubscriptionAdmin(Subscription, admin.site)
        Subscription.objects.create(name='Henrique Bastos',
            cpf='12345678901', email='henrique@bastos.net')

    def test_has_action(self):
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        """Mark as paid"""
        fake_request = Mock()
        queryset = Subscription.objects.all()
        self.model_admin.mark_as_paid(fake_request, queryset)

        self.assertEqual(1, Subscription.objects.filter(paid=True).count())
# coding:utf-8

from datetime import datetime

from django.test import TestCase
from django.db import IntegrityError
from django.core.urlresolvers import reverse


class SubscriptionTest(TestCase):
    def setUp(self):
        from subscriptions.models import Subscription

        self.obj = Subscription(
            name='Italo Maia',
            cpf='1234567890',
            email='algo@algo.com',
            phone='2345678')

    def test_create(self):
        self.obj.save()
        self.assertEqual(1, self.obj.id)

    def test_has_created_at(self):
        """
        Subscription must have automatic created_at
        """
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_cpf_unique(self):
        from subscriptions.models import Subscription

        self.obj.save()
        s = Subscription(
            name='Italo Maia',
            cpf='1234567890',
            email='outro@algo.com',
            phone='2345678')
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        from subscriptions.models import Subscription

        self.obj.save()
        s = Subscription(
            name='Italo Maia',
            cpf='0123456789',
            email='algo@algo.com',
            phone='2345678')
        self.assertRaises(IntegrityError, s.save)

    def test_unicode(self):
        from subscriptions.models import Subscription

        self.assertEqual(u'Italo Maia', unicode(self.obj))

    def test_permalink(self):
        self.obj.save()
        self.assertIsInstance(self.obj.get_absolute_url(), basestring)

    def test_permalink_has_id(self):
        self.obj.save()
        self.assertIn(str(self.obj.pk), self.obj.get_absolute_url())

    def test_paid_default_value_is_false(self):
        self.assertEqual(False, self.obj.paid)


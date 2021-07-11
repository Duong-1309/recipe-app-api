from django.test import TestCase

from app.func import add


class FuncTests(TestCase):

    def test_add_numbers(self):
        """ Test that two numbers are added together"""
        self.assertEqual(add(5,5), 10)
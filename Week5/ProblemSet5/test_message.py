from unittest import TestCase
from Week5.ProblemSet5.ps6 import *


class TestMessage(TestCase):
    def test_apply_shift(self):
        a = Message('hello')
        b = Message('stuvwxyz')
        self.assertEqual(a.apply_shift(5), 'mjqqt', "Should be 'mjqqt'")
        self.assertEqual(b.apply_shift(10), 'cdefghij')


class TestPlaintextMessage(TestCase):
    a = PlaintextMessage('hello', 5)

    def test_get_shift(self):
        self.assertEqual(self.a.get_shift(), 5)

    def test_get_encrypting_dict(self):
        # self.assertEqual(self.)
        pass

    def test_get_message_text_encrypted(self):
        self.assertEqual(self.a.get_message_text_encrypted(), 'mjqqt')

    def test_change_shift(self):
        b = PlaintextMessage('hello', 5)
        b.change_shift(6)
        self.assertEqual(b.get_message_text_encrypted(), 'nkrru')
        b.change_shift(10)
        self.assertEqual(b.get_message_text_encrypted(), 'rovvy')

import unittest

from proj import ClassA
from proj.moduleB import ClassB

class Inclusion(unittest.TestCase):

    # Both classes are accessable
    def test_A(self):
        m = ClassA('x')
        self.assertEqual('x', m.get_x())

    def test_B(self):
        m = ClassB('x')
        self.assertEqual('x', m.get_x())

    # Can't import ClassB directly, since it's not mentioned in proj/__init__.py
    def test_direct_class(self):
        with self.assertRaises(ImportError):
            from proj import ClassB

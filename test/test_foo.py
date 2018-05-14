import unittest
import proj

class Bar(unittest.TestCase):

    # This test pases
    def test_qux(self):
        self.assertEqual('quux', proj.Qux.Quux())

    # This test fails
    def test_baz(self):
        self.assertEqual('baz', proj.Qux.Quux(), msg='this test should fail')

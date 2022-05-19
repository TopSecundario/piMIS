import unittest

from example import sayHello


class TestExample(unittest.TestCase):

    def test_sayHello(self):
        self.assertEqual('python', sayHello('python'))

import unittest
from recordlocator import generator


class TestGenerator(unittest.TestCase):

    def test_default_generation(self):
        """ The default locator length is 8. """

        locator = generator.generate()
        self.assertEqual(len(locator), 8)
        self.assertTrue(locator.isupper())

import unittest
from recordlocator import generator


class TestGenerator(unittest.TestCase):

    def test_default_generation(self):
        """ The default locator length is 8. Also check some basic things
        about the locator. """

        locator = generator.safe_generate()
        self.assertEqual(len(locator), 8)
        self.assertTrue(locator.isupper())
        for c in ['B', '8', '5', 'S', '0', 'O', '1', 'I', 'Q']:
            self.assertTrue(c not in locator)

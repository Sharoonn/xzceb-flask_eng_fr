'''language testing module'''

import unittest
from translator import english_to_french, french_to_english


class MyModuleTest(unittest.TestCase):
    '''translation testing class'''
    def test_e2f(self):
        '''testing english to french translation'''
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Hello"), "Hello")


    def test_f2e(self):
        '''testing french to english translation'''
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")

if __name__ == "__main__":
    unittest.main()
    
import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour") 
        self.assertEqual(english_to_french("what is your name?"), "quel est ton nom ?")  
        self.assertNotEqual(english_to_french(""), "")  


class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello") 
        self.assertEqual(french_to_english("quel est ton nom ?"), "what is your name?") 
        self.assertEqual(french_to_english(""), "") 

unittest.main()
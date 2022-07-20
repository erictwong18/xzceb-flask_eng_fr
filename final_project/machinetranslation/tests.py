import unittest

from translator import french_to_english, english_to_french

class TestFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(''),'') # Null input text
        self.assertEqual(french_to_english('Bonjour'),'Hello') # "Bonjour" to "Hello" Translation Test
        

class TestDouble(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(''),'') # Null input text
        self.assertEqual(english_to_french('Hello'),'Bonjour') # "Bonjour" to "Hello" Translation Test        

unittest.main()
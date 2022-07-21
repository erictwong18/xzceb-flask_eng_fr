import unittest
from translator import french_to_english, english_to_french

class TestFrenchNull(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(french_to_english(''),'') # Null input text

class TestFrenchTranslate(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'),'Hello') # "Bonjour" to "Hello" Translation Test        

class TestEnglishNull(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french(''),'') # Null input text
        
class TestEnglishTranslate(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'),'Bonjour') # "Hello" to "Bonjour" Translation Test      

unittest.main()
# test/test_unittest.py

import unittest
from src.text_analyzer import count_words, count_characters, count_sentences, analyze_text

class TestTextAnalyzer(unittest.TestCase):

    def test_count_words(self):
        """Test the word count function."""
        self.assertEqual(count_words("Hello world"), 2)
        self.assertEqual(count_words("This is a test."), 4)
        self.assertEqual(count_words(""), 0)

    def test_count_characters(self):
        """Test the character count function."""
        self.assertEqual(count_characters("Hello"), 5)
        self.assertEqual(count_characters("Hello world"), 11)
        self.assertEqual(count_characters(""), 0)

    def test_count_sentences(self):
        """Test the sentence count function."""
        self.assertEqual(count_sentences("Hello world. This is a test!"), 2)
        self.assertEqual(count_sentences("Is this one? Yes!"), 2)
        self.assertEqual(count_sentences("No punctuation here"), 0)

    def test_analyze_text(self):
        """Test the main analysis summary function."""
        sample_text = "First sentence. Second sentence!"
        expected = {
            'word_count': 4,
            'character_count': 32,
            'sentence_count': 2
        }
        self.assertDictEqual(analyze_text(sample_text), expected)

if __name__ == '__main__':
    unittest.main()
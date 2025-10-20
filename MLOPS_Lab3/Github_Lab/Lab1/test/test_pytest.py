# test/test_pytest.py

from src.text_analyzer import count_words, count_characters, count_sentences, analyze_text

def test_count_words():
    """Test the word count function."""
    assert count_words("Hello world") == 2
    assert count_words("This is a test.") == 4
    assert count_words("") == 0

def test_count_characters():
    """Test the character count function."""
    assert count_characters("Hello") == 5
    assert count_characters("Hello world") == 11 # spaces are counted
    assert count_characters("") == 0

def test_count_sentences():
    """Test the sentence count function."""
    assert count_sentences("Hello world. This is a test!") == 2
    assert count_sentences("Is this the first sentence? Yes, it is.") == 2
    assert count_sentences("No punctuation here") == 0

def test_analyze_text():
    """Test the main analysis summary function."""
    sample_text = "First sentence. Second sentence!"
    expected = {
        'word_count': 4,
        'character_count': 32,
        'sentence_count': 2
    }
    assert analyze_text(sample_text) == expected
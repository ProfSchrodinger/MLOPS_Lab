import re

def count_words(text):
    """Counts the number of words in a given text."""
    if not isinstance(text, str):
        return 0
    words = text.split()
    return len(words)

def count_characters(text):
    """Counts the total number of characters, including spaces."""
    if not isinstance(text, str):
        return 0
    return len(text)

def count_sentences(text):
    """Counts the number of sentences based on ., !, ? delimiters."""
    if not isinstance(text, str):
        return 0
    sentences = re.findall(r'[^.!?]+[.!?]', text)
    return len(sentences)

def analyze_text(text):
    """Provides a summary dictionary of text analysis."""
    if not isinstance(text, str):
        return {}
    analysis = {
        'word_count': count_words(text),
        'character_count': count_characters(text),
        'sentence_count': count_sentences(text)
    }
    return analysis
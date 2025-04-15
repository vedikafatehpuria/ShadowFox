from spellchecker import SpellChecker

spell = SpellChecker()

def correct_word(word):
    """
    Autocorrect a single word using pyspellchecker.
    """
    return spell.correction(word)

def correct_sentence(sentence):
    """
    Autocorrect all words in a sentence.
    """
    words = sentence.split()
    corrected = [correct_word(w) for w in words]
    return " ".join(corrected)

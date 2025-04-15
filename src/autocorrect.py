from spellchecker import SpellChecker

spell = SpellChecker()

def correct_word(word):
    correction = spell.correction(word)
    return correction

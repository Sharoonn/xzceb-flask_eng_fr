'''translation function modules'''
from deep_translator import MyMemoryTranslator

frn_traslator = MyMemoryTranslator(source='en', target='fr')

def english_to_french(english_text):
    '''converts english string to french string'''
    french_text = frn_traslator.translate(english_text)
    return french_text


eng_traslator = MyMemoryTranslator(source='fr', target='en')

def french_to_english(french_text):
    '''converts french string to english string'''
    english_text = eng_traslator.translate(french_text)
    return english_text

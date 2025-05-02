from deep_translator import GoogleTranslator

def translate_to_urdu(text):
    return GoogleTranslator(source='auto', target='ur').translate(text)

def simplify_english_for_tts(text):
    replacements = {
        "highly sensitive": "affected easily",
        "fertilizer levels": "amount of fertilizer",
        "proper use": "good use",
        "significantly increase": "help increase",
        "the yield": "crop harvest",
        "timely irrigation": "watering at the right time",
        "plays a crucial role": "is very important",
        "healthy plant development": "good plant growth",
        "phosphorus": "phosphorus fertilizer",
        "nitrogen": "nitrogen fertilizer",
        "potassium": "potassium fertilizer",
        "to address": "to fix",
        "I recommend": "you should",
        "additionally": "also"
    }

    for word, simple in replacements.items():
        text = text.replace(word, simple)

    text = text.replace(" and ", ". ")
    text = text.replace(" but ", ". ")

    return text

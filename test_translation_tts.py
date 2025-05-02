from deep_translator import GoogleTranslator
from elevenlabs import ElevenLabs
import os

# ✅ Set your ElevenLabs API key
client = ElevenLabs(
    api_key="sk_4ac2e2e10d70a570f8d4c4206ce4b356d5ceb01a49d54bc2"  # 🔴 Replace with your real API key
)

# ✅ Helper function to simplify English for better translation and speech
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

# ✅ Function to translate English ➔ Urdu using deep-translator
def translate_to_urdu(text):
    return GoogleTranslator(source='auto', target='ur').translate(text)

# ✅ Function to generate Urdu speech using the new ElevenLabs client
def generate_urdu_speech_elevenlabs(text, output_path="urdu_crop_advice.mp3"):
    try:
        audio_stream = client.generate(
            text=text,
            voice="Rachel"
        )

        with open(output_path, "wb") as f:
            for chunk in audio_stream:
                f.write(chunk)

        print(f"✅ Urdu MP3 saved at: {output_path}")

    except Exception as e:
        print(f"❌ Failed to generate Urdu speech with ElevenLabs: {e}")

# ✅ Sample English Text
english_text = """
The cotton crop is highly sensitive to fertilizer levels.
Proper use of nitrogen and phosphorus fertilizers can significantly increase the yield.
Timely irrigation also plays a crucial role in healthy plant development.
"""

# ✅ Step 1: Simplify English
simple_english = simplify_english_for_tts(english_text)
print("📝 Simplified English Text:\n", simple_english)

# ✅ Step 2: Translate to Urdu
urdu_text = translate_to_urdu(simple_english)
print("🔁 Urdu Translation:\n", urdu_text)

# ✅ Step 3: Generate Urdu Speech
generate_urdu_speech_elevenlabs(urdu_text, "urdu_crop_advice.mp3")

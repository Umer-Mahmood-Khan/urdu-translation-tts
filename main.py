from utils.simplify import simplify_english_for_tts
from utils.translation import translate_to_urdu
from utils.tts import generate_urdu_speech_elevenlabs

# ✅ Sample English Text
english_text = """
During the Squaring stage, it is advisable to address the nutrient issues identified in the field report.
Nitrogen is slightly low, which can be corrected by applying 50 kg/acre Urea. Phosphorus is severely low,
and it is important to apply 35 kg/acre MAP to improve the phosphorus content in the soil.
Potassium is also severely low, and it is recommended to apply 30 kg/acre Potassium Sulfate to maintain optimal potassium levels.
In addition to these fertilizers, it is important to improve soil health by incorporating compost or organic matter into the soil. This will enhance soil structure, increase water retention, and promote beneficial microorganisms that aid plant growth. It is advisable to apply Gypsum to improve soil structure and pH balance.
"""

# ✅ Step 1: Simplify English
simple_english = simplify_english_for_tts(english_text)
print("📝 Simplified English Text:\n", simple_english)

# ✅ Step 2: Translate to Urdu
urdu_text = translate_to_urdu(simple_english)
print("🔁 Urdu Translation:\n", urdu_text)

# ✅ Step 3: Generate Urdu Speech
generate_urdu_speech_elevenlabs(urdu_text, "examples/output_audio.mp3")

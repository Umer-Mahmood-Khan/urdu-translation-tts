from elevenlabs import ElevenLabs
import os

client = ElevenLabs(
    api_key="YOUR_API_KEY"  # 🔴 Replace this with your real API key
)

def generate_urdu_speech_elevenlabs(text, output_path="urdu_crop_advice.mp3"):
    try:
        audio_stream = client.generate(
            text=text,
            voice="Rachel"
        )

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, "wb") as f:
            for chunk in audio_stream:
                f.write(chunk)

        print(f"✅ Urdu MP3 saved at: {output_path}")

    except Exception as e:
        print(f"❌ Failed to generate Urdu speech with ElevenLabs: {e}")

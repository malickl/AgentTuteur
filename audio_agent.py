from google import genai
from google.genai import types
import wave
import os 
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

class GeminiAudioAgent:
   def __init__(self):
      self.geminiclient = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

   def write_wav_file(self, filename, pcm, channels=1, rate=24000, sample_width=2):
      with wave.open(filename, "wb") as wf:
         wf.setnchannels(channels)
         wf.setsampwidth(sample_width)
         wf.setframerate(rate)
         wf.writeframes(pcm)

   def generate_audio(self, message_to_audio):
      response = self.geminiclient.models.generate_content(
         model="gemini-2.5-flash-preview-tts",
         contents=message_to_audio,
         config=types.GenerateContentConfig(
               response_modalities=["AUDIO"],
               speech_config=types.SpeechConfig(
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                           voice_name='Kore',
                     )
                  )
               ),
         )
      )

      data = response.candidates[0].content.parts[0].inline_data.data

      file_name = "resume.wav"
      self.write_wav_file(file_name, data)

      # 🔥 lire le vrai wav pour Streamlit
      with open(file_name, "rb") as f:
         wav_bytes = f.read()

      return wav_bytes


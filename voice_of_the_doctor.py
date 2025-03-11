# ✅ Import Required Libraries
import os
import subprocess
import platform
from gtts import gTTS
from pydub import AudioSegment

# ✅ Function: Convert Text to Speech using gTTS
def text_to_speech_with_gtts(input_text, mp3_filepath="gtts_output.mp3", wav_filepath="gtts_output.wav"):
    try:
        language = "en"
        tts = gTTS(text=input_text, lang=language, slow=False)
        tts.save(mp3_filepath)
        print(f"✅ gTTS Audio Saved: {mp3_filepath}")

        # 🔄 Convert MP3 to WAV (for compatibility with Windows Media.SoundPlayer)
        convert_mp3_to_wav(mp3_filepath, wav_filepath)

        # 🔊 Play the generated speech
        play_audio(wav_filepath)

    except Exception as e:
        print(f"❌ Error in gTTS: {e}")

# ✅ Function: Convert MP3 to WAV
def convert_mp3_to_wav(mp3_filepath, wav_filepath):
    try:
        audio = AudioSegment.from_mp3(mp3_filepath)
        audio.export(wav_filepath, format="wav")
        print(f"✅ Converted MP3 to WAV: {wav_filepath}")
    except Exception as e:
        print(f"❌ Error converting MP3 to WAV: {e}")

# ✅ Function: Play the Saved Audio File
def play_audio(audio_file):
    try:
        os_name = platform.system()

        if os_name == "Darwin":  # macOS
            subprocess.run(["afplay", audio_file])
        elif os_name == "Windows":  # Windows
            subprocess.run(["powershell", "-c", f'(New-Object Media.SoundPlayer \"{audio_file}\").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(["aplay", audio_file])  # Alternative: 'mpg123', 'ffplay'
        else:
            raise OSError("Unsupported operating system")

        print(f"🔊 Playing: {audio_file}")

    except Exception as e:
        print(f"❌ Error while playing audio: {e}")

# ✅ Example Usage
if __name__ == "__main__":
    input_text = "Hello, this is an AI-generated voice using gTTS with a fixed audio playback issue."
    text_to_speech_with_gtts(input_text)

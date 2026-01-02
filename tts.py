import subprocess
import platform
from gtts import gTTS


def play_audio(filepath):
    os_name = platform.system()
    if os_name == "Darwin":
        subprocess.run(["afplay", filepath])
    elif os_name == "Windows":
        subprocess.run(
            ["powershell", "-c", f'(New-Object Media.SoundPlayer "{filepath}").PlaySync();']
        )
    elif os_name == "Linux":
        subprocess.run(["aplay", filepath])


def text_to_speech(input_text, output_filepath="speech.mp3"):
    tts = gTTS(text=input_text, lang="en", slow=False)
    tts.save(output_filepath)
    play_audio(output_filepath)


# TEST
if __name__ == "__main__":
    text_to_speech(
        "hi, myself Saarthi."
    )

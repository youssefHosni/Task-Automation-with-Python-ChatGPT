import sys
from gtts import gTTS

def convert_text_to_audio(text, output_file):
    # Create a gTTS object with the text and desired language
    tts = gTTS(text=text, lang='en')

    # Save the audio to a file
    tts.save(output_file)
    print(f"Audio file saved as {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <text_file_path> <output_audio_file_path>")
        sys.exit(1)

    text_file_path = sys.argv[1]
    output_audio_file = sys.argv[2]

    # Read the text from the file
    with open(text_file_path, 'r') as file:
        text = file.read()

    # Convert text to audio
    convert_text_to_audio(text, output_audio_file)
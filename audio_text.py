import sys
import speech_recognition as sr

def convert_audio_to_text(audio_file):
    # Initialize the recognizer
    r = sr.Recognizer()
    
    # Load the audio file
    with sr.AudioFile(audio_file) as source:
        # Read the audio data from the file
        audio_data = r.record(source)
        
        try:
            # Use the recognizer to convert audio to text
            text = r.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from the speech recognition service; {e}")
    
    return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <audio_file_path>")
        sys.exit(1)
    
    audio_file_path = sys.argv[1]
    
    # Convert audio to text
    result = convert_audio_to_text(audio_file_path)
    
    if result:
        # Print the converted text
        print(result)

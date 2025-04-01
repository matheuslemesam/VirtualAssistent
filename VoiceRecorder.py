import sounddevice as sd
import numpy as np
import wave
import whisper

DEFAULT_LANGUAGE = "pt"  # Default language for transcription
SAMPLE_RATE = 44100  # Sample rate for audio recording
CHANNELS = 2  # Number of audio channels
SAMPLE_WIDTH = 2  # Sample width in bytes

def record_audio(seconds=10, filename="recorded_audio.wav"):
    """
    Record audio locally and save it as a WAV file.
    
    Parameters:
    seconds (int): Duration of the recording in seconds.
    filename (str): Name of the output WAV file.
    
    Returns:
    str: Path to the saved WAV file.
    """
    print(f"Recording for {seconds} seconds...")
    audio = sd.rec(int(seconds * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=CHANNELS, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("Recording finished. Saving audio...")

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(SAMPLE_WIDTH)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(audio.tobytes())
    
    print(f"Audio saved as {filename}")
    return filename

def transcribe_audio(filename, language=DEFAULT_LANGUAGE, model_size="small"):
    """
    Transcribe audio using the Whisper model.
    
    Parameters:
    filename (str): Path to the WAV file to transcribe.
    language (str): Language of the audio for transcription.
    model_size (str): Size of the Whisper model to use (e.g., tiny, small, medium, large).
    
    Returns:
    str: Transcribed text from the audio.
    """
    print(f"Loading Whisper model ({model_size})...")
    model = whisper.load_model(model_size)
    print("Transcribing audio...")
    result = model.transcribe(filename, fp16=False, language=language)
    print("Transcription completed.")
    return result.get("text", "")

def main():
    """
    Main function to record and transcribe audio.
    """
    try:
        # Step 1: Record audio
        audio_file = record_audio(seconds=10, filename="recorded_audio.wav")
        
        # Step 2: Transcribe the recorded audio
        transcription = transcribe_audio(audio_file, language=DEFAULT_LANGUAGE)
        
        # Step 3: Display the transcription
        print("Transcribed Text:")
        print(transcription)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
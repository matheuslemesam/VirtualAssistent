import sounddevice as sd
import numpy as np
import wave
import whisper

language = "pt"  # Portuguese

def record_audio(seconds=10, filename="recorded_audio.wav"):
    """
    Record audio locally and save it as a WAV file.
    
    Parameters:
    seconds (int): Duration of the recording in seconds.
    filename (str): Name of the output WAV file.
    
    Returns:
    str: Path to the saved WAV file.
    """
    print("Recording...")
    fs = 44100  # Sample rate
    audio = sd.rec(int(seconds * fs), samplerate=fs, channels=2, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("Recording finished.")

    # Save as WAV file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(fs)
        wf.writeframes(audio.tobytes())
    print(f"Audio saved as {filename}")
    return filename

def transcribe_audio(filename, language="pt"):
    """
    Transcribe audio using the Whisper model.
    
    Parameters:
    filename (str): Path to the WAV file to transcribe.
    language (str): Language of the audio for transcription.
    
    Returns:
    str: Transcribed text from the audio.
    """
    print("Loading Whisper model...")
    model = whisper.load_model("small")  # Options: tiny, medium, large
    print("Transcribing audio...")
    result = model.transcribe(filename, fp16=False, language=language)
    print("Transcription completed.")
    return result["text"]

# Main flow
if __name__ == "__main__":
    # Step 1: Record audio
    audio_file = record_audio(seconds=10, filename="recorded_audio.wav")
    
    # Step 2: Transcribe the recorded audio
    transcription = transcribe_audio(audio_file, language="pt")
    
    # Step 3: Display the transcription
    print("Transcribed Text:")
    print(transcription)
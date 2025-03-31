import sounddevice as sd
import numpy as np
import wave

def record_audio_local(seconds=5, filename="recorded_audio.wav"):
    """
    Record audio locally and save it as a WAV file.
    
    Parameters:
    seconds (int): Duration of the recording in seconds.
    filename (str): Name of the output WAV file.
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

record_audio_local()
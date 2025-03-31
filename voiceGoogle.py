from IPython.display import Audio, display, Javascript
from google.colab import output
from base64 import b64encode

RECORD = """
const sleep = time => new Promise(resolve => setTimeout(resolve, time));

const b2text = blob => new Promise(resolve => {
    const reader = new FileReader();
    reader.onloadend = e => resolve(e.srcElement.result);
    reader.readAsDataURL(blob);
});

var record = time => new Promise(async resolve => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const recorder = new MediaRecorder(stream);
    const chunks = [];

    recorder.ondataavailable = e => chunks.push(e.data);
    recorder.start();

    await sleep(time);

    recorder.onstop = async () => {
        const blob = new Blob(chunks);
        const text = await b2text(blob);
        resolve(text);
    };

    recorder.stop();
});
"""

def record_audio(seconds=5):
    """
    Record audio for a specified number of seconds and return the base64 encoded string.
    
    Parameters:
    seconds (int): Duration of the recording in seconds. Default is 5 seconds.
    
    Returns:
    str: Base64 encoded string of the recorded audio.
    """
    display(Javascript(RECORD))
    output.eval_js(f"record({seconds * 1000})")  # Convert seconds to milliseconds
    audio_data = output.eval_js("record")
    
    if audio_data:
        return audio_data.split(',')[1]  # Return only the base64 part
    else:
        raise ValueError("Audio recording failed.")
    
    file_name = "recorded_audio.wav"
    with open(file_name, "wb") as f:
        f.write(b64decode(audio_data))

    return f'/content/{file_name}'

print("Recording audio...")

record_file = record_audio()
display(Audio(record_file, autoplay=True))
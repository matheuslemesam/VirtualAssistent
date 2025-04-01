# VirtualAssistent
Repository created for studies and development of an intelligent virtual assistant that recognizes voice and returns me what I need.

# Tecnologies used
- Python
- JavaScript

# Installation
*Windows:*

    - Bash:

        - pip install sounddevice

        - pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

        - pip install openai-whisper

        - pip install openai

    - Browser:
        - https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip (extract and add to path)

*Ubuntu*

    - Bash:

        Update the system:
            sudo apt update && sudo apt upgrade -y

        Install basic dependencies:
            sudo apt install python3-pip python3-venv ffmpeg -y

        To check if ffmpeg was installed correctly, run:
            ffmpeg -version

        Create and activate a virtual environment (venv):
            python3 -m venv venv
            source venv/bin/activate

        Install the packages inside the virtual environment:
            pip install --upgrade pip
            sudo apt install portaudio19-dev -y
            pip install sounddevice
            pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
            pip install openai-whisper
            pip install openai

        Test if everything was installed correctly:
            python -c "import torch; print(torch.__version__)"
            python -c "import sounddevice; print(sounddevice.__version__)"
            python -c "import whisper; print(whisper.__version__)"
            python -c "import openai; print(openai.__version__)"
    
        Audio playing:
            aplay file.wav


# Steps for developing
1. Voice recorder with Python and JavaScript
2. Voice recognition with Python and library Whisper(OpenAI)
3. integrate with ChatGPT API
4. Synthesizing chat gpt response into voice using library gTTS
import whisper

model = whisper.load_model("small") #tiny, medium, large

result = model.transcribe("record", fp16=False, language=language)
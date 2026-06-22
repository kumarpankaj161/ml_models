import whisper

model = whisper.load_model("large-v2")
#result = model.transcribe(audio = "audios/0 - Programming Tutorial.mp3",
#                          language = "hi",
#                          task = "translate")
#print(result["text"])
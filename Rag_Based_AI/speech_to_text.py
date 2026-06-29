import whisper
import json

model = whisper.load_model("base")
result = model.transcribe(audio = r"C:\Users\pk362\ML_MODEL\Rag_Based_AI\audios\0 - Programming Tutorial.mp3",
                         language = "en",
                         task = "translate",
                         word_timestamps=False)
#print(result["segments"])
chunks = []
for segment in result["segments"]:
    chunks.append({"start": segment["start"], "end": segment["end"], "text": segment["text"]})

print(chunks)

with open("output.json", "w") as f:
    json.dump(chunks,f)

 



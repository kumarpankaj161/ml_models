import whisper
import json
import os
#

model = whisper.load_model("base")

mp3s = os.listdir("Rag_Based_AI/audios")

for audio in mp3s:      
    number = audio.split("-")[0]
    title = audio.split("-")[1][:-4]
    print(number, title)
    result = model.transcribe(audio = f"Rag_Based_AI/audios/{audio}",
                         language = "en",
                         task = "translate",
                         word_timestamps=False)
    chunks = []
    for segment in result["segments"]:
        chunks.append({"number" : number,"title" : title ,"start": segment["start"], "end": segment["end"], "text": segment["text"]})

    chunks_with_metadata = {"chunks": chunks, "text": result["text"]}

    with open(f"C:/Users/pk362/ML_MODEL/Rag_Based_AI/jsons/{audio}.json", "w") as f:
        json.dump(chunks_with_metadata,f)

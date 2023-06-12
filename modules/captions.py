from datetime import timedelta
import os
import whisper

def transcribe_audio(path):
    model = whisper.load_model("small") 
    print("Whisper model loaded.")
    transcribe = model.transcribe(audio=path)
    segments = transcribe['segments']

    video_filename = os.path.splitext(os.path.basename(path))[0]

    for segment in segments:
        print(segment)
        startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
        endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
        text = segment['text']
        segmentId = segment['id']+1
        segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"

        srtFilename = os.path.join("../SrtFiles", f"{video_filename}.srt")
        with open(srtFilename, 'a', encoding='utf-8') as srtFile:
            srtFile.write(segment)

    return srtFilename


if __name__ == "__main__":
    transcribe_audio('./testVid.mp4')
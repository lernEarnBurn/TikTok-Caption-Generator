import os
import whisper
from datetime import timedelta

def transcribe_audio(path, max_words_per_segment):
    model = whisper.load_model("small") 
    print("Whisper model loaded.")
    transcribe = model.transcribe(audio=path)
    segments = transcribe['segments']

    video_filename = os.path.splitext(os.path.basename(path))[0]

    for segment in segments:
        startTime = str(0) + str(timedelta(seconds=int(segment['start']))) + ',000'
        endTime = str(0) + str(timedelta(seconds=int(segment['end']))) + ',000'
        text = segment['text']
        segmentId = segment['id'] + 1

        words = text.split()
        num_words = len(words)
        chunk_size = min(max_words_per_segment, num_words)
        num_segments = num_words // chunk_size + (num_words % chunk_size > 0)

        for i in range(num_segments):
            start_index = i * chunk_size
            end_index = (i + 1) * chunk_size
            chunk_text = ' '.join(words[start_index:end_index])

            segment = f"{segmentId}\n{startTime} --> {endTime}\n{chunk_text[1:] if chunk_text[0] == ' ' else chunk_text}\n\n"

            srtFilename = os.path.join("SrtFiles", f"{video_filename}.srt")
            with open(srtFilename, 'a', encoding='utf-8') as srtFile:
                srtFile.write(segment)

            segmentId += 1

    return srtFilename


if __name__ == "__main__":
    transcribe_audio('./testVid.mp4', max_words_per_segment=6)
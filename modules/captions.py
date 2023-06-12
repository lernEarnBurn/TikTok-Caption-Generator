from datetime import timedelta
import os
import whisper
import datetime 

from datetime import datetime, timedelta

def transcribe_audio(path):
    model = whisper.load_model("small") 
    print("Whisper model loaded.")
    transcribe = model.transcribe(audio=path)
    segments = transcribe['segments']

    video_filename = os.path.splitext(os.path.basename(path))[0]

    for segment in segments:
        start_time = timedelta(seconds=float(segment['start']))
        end_time = timedelta(seconds=float(segment['end']))

        start_datetime = datetime(1, 1, 1) + start_time
        end_datetime = datetime(1, 1, 1) + end_time

        start_time_formatted = start_datetime.strftime("%H:%M:%S,%f")[:-3]
        end_time_formatted = end_datetime.strftime("%H:%M:%S,%f")[:-3]

        text = segment['text']
        segment_id = segment['id'] + 1
        segment_content = f"{segment_id}\n{start_time_formatted} --> {end_time_formatted}\n{text[1:] if text[0] == ' ' else text}\n\n"

        srt_filename = os.path.join("./SrtFiles", f"{video_filename}.srt")
        with open(srt_filename, 'a', encoding='utf-8') as srt_file:
            srt_file.write(segment_content)

    print('\n\nSRT generated')

    return srt_filename
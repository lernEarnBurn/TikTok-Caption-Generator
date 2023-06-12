from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import os
import pysrt
from datetime import datetime as dt
from .videoSize import get_video_dimensions

os.environ["IMAGEIO_FFMPEG_EXE"] = r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\ffmpeg.exe"

def add_caption_overlay(video_path, srt_path):
    video_filename = os.path.splitext(os.path.basename(video_path))[0]

    video = VideoFileClip(video_path)

    subs = pysrt.open(srt_path)

    reference_date = dt(1900, 1, 1)

    clips = []

    for caption in subs:
        start_time = dt.combine(reference_date, caption.start.to_time())
        start_time_float = (start_time - reference_date).total_seconds()
        end_time = dt.combine(reference_date, caption.end.to_time())
        caption_text = caption.text_without_tags

        duration_seconds = (end_time - start_time).total_seconds()

        screensize = get_video_dimensions(video_path)
        

        text = TextClip(caption_text, fontsize=55, color='white', font='Corbel', method='caption', stroke_color='white', stroke_width=2.5, size=screensize)

        text = text.set_position(('center')).set_start(start_time_float).set_duration(duration_seconds)

        clips.append(text)

    final_clip = CompositeVideoClip([video] + clips)
    final_clip = final_clip.set_duration(video.duration)
    final_clip.write_videofile(f'./output/{video_filename}.mp4', codec='libx264', audio_codec='aac')

    
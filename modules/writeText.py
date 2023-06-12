from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import os
import pysrt
from datetime import datetime as dt

os.environ["IMAGEIO_FFMPEG_EXE"] = r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\ffmpeg.exe"

def add_caption_overlay(video_path, srt_path):
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

        text = TextClip(caption_text, fontsize=55, color='white', font='Corbel', method='caption', stroke_color='white', stroke_width=2.0)

        text = text.set_position(('center')).set_start(start_time_float).set_duration(duration_seconds)

        clips.append(text)

    final_clip = CompositeVideoClip([video] + clips)
    final_clip = final_clip.set_duration(video.duration)
    final_clip.write_videofile('../output/testVid.mp4', codec='libx264', audio_codec='aac')

if __name__ == "__main__":
    add_caption_overlay('../testVid.mp4', '../srtFiles/testVid.srt')
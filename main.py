from modules.captions import transcribe_audio
from modules.writeText import add_caption_overlay
import tkinter as tk
from tkinter import filedialog
import os



def main():
    root = tk.Tk()
    root.withdraw()  

    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    transcribe_audio(file_path)
    add_caption_overlay(file_path, f'./srtFiles/{file_name}.srt')

    print('\n\nVideo Complete')

if __name__ == "__main__" :
    main()
    #add_caption_overlay('./testVid.mp4', './srtFiles/testVid.srt')
    #transcribe_audio('./testVid.mp4')
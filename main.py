from captions import transcribe_audio
import tkinter as tk
from tkinter import filedialog


def main():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open a file selection dialog
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
    transcribe_audio(file_path)

if __name__ == "__main__" :
    main()
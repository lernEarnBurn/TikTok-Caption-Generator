# Shorts-Caption-Generator
A caption generator where you input a youtube shorts/Tik Tok 9:16 video, and the whisper api generates captions and openCV displays them.
Whispers accuracy depends which model you select, which will be constrained by GPU power.
Will implement interface to edit text position and style.

In order to shorten each Token in Whisper I tweaked the source code 
see https://github.com/openai/whisper/discussions/223 for details.

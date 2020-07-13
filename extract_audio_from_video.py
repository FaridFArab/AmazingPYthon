# moviepy

import moviepy.editor

video = moviepy.editor.VideoFileClip("samplevide.mp4")
audio = video.audio
audio.write_audiofile("result_audio.mp3")
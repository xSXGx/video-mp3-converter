# pip install moviepy
import moviepy.editor

# read video file
video = moviepy.editor.VideoFileClip("video_name.mp4")

# convert video data to audio
audio = video.audio

# save audio file
audio.write_audiofile("audio_name.mp3")

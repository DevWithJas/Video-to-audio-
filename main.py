
import moviepy.editor as mp
from numpy import clip

clip = mp.VideoFileClip("D:\\PYTHON BASIC PROJECTS\\Video to audio Converter\\Tony-Stark-Attitude-Full-Screen-WhatsApp-Status-Video-1.mp4")
clip.audio.write_audiofile("my Audio.mp3")
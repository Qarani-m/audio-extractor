import subprocess
from moviepy.editor import *



class Extractor:
    def __init__(self,inputfile):
        self.inputfile= inputfile
        self.output_file_name= self.get_output_file_name()
        pass
    def test(self):
        print("stuff")
    def get_output_file_name(self):
        return "name"
    def moviepy_way(self):
        input_file = "/home/martin/Music/video/(6) Jidenna - Bambi - YouTube.mkv"
        output_file = "/home/martin/Music/sample.mp3"
        video_clip = VideoFileClip(self.inputfile)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(output_file)
    def ffmpeg_way(self):
        input_file = "/home/martin/Music/video/it'll be ok.mkv"
        output_file = "sample.mp3"
        subprocess.run(["ffmpeg", "-i", input_file, "-vn", "-acodec", "libmp3lame", "-ab", "128k", "-ar", "44100", output_file])


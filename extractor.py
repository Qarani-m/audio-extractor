import subprocess
from moviepy.editor import *
class Extractor:
    def __init__(self,inputfile, output_file_name,output_folder):
        self.inputfile= inputfile
        self.output_folder = output_folder
        self.output_file_name = output_file_name
        print(self.output_file_name)
    def get_output_file_name(self):
        return "name"
    def moviepy_way(self):
        try:
            video_clip = VideoFileClip(self.inputfile)
            audio_clip = video_clip.audio
            stuf=audio_clip.write_audiofile(f"{self.output_folder}/{self.output_file_name}")
            
        except Exception as e:
            print(e)
            self.ffmpeg_way()
    def ffmpeg_way(self):
        try:
            output_file = f"{self.output_folder}/{self.output_file_name}"
            subprocess.run(["ffmpeg", "-i", self.inputfile, "-vn", "-acodec", "libmp3lame", "-ab", "128k", "-ar", "44100", output_file])
        except Exception as e:
            print(e)
            self.moviepy_way()
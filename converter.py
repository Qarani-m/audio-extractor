import subprocess
from moviepy.editor import *



class Extractor:
    def __init__(self,inputfile, output_file_name,output_folder):
        self.inputfile= inputfile
        self.output_folder = output_folder
        self.output_file_name = output_file_name
        self.output_file_name= self.get_output_file_name()
        print(self.output_file_name)

    def test(self):
        print("stuff")
    def get_output_file_name(self):
        return "name"
    def moviepy_way(self):
        pass
        # video_clip = VideoFileClip(self.inputfile)
        # audio_clip = video_clip.audio
        # audio_clip.write_audiofile(f"{self.output_folder}/{self.output_file_name}.mp3")
    def ffmpeg_way(self):
        input_file = "/home/martin/Music/video/it'll be ok.mkv"
        output_file = "sample.mp3"
        subprocess.run(["ffmpeg", "-i", input_file, "-vn", "-acodec", "libmp3lame", "-ab", "128k", "-ar", "44100", output_file])


from pathlib import Path
import platform
import os
from extractor import Extractor

class Saving_file:
    def __init__(self, input_file):
        self.input_file=input_file
        self.home = str(Path.home())
        self.create_destination_folder()
    def save(self):
        output_array=self.input_file.split("/")
        filename=f"{output_array[len(output_array)-1].split('.')[0]}.mp3"
        destination = f"{self.home}/Music/Em Audio extractor"
        return [filename,destination]
    def create_destination_folder(self):
        if not os.path.exists(f"{self.home}/Music/Em Audio extractor"):
            os.makedirs(f"{self.home}/Music/Em Audio extractor")

    def handle_files(file):
        file_name =file
        file=Saving_file(file_name).save()
        extractor = Extractor(file_name,file[0],file[1])
        extractor.moviepy_way()
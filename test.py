from pathlib import Path
import platform
import os
input_file = "/home/martin/Music/video/(6) Jidenna - Bambi - YouTube.mkv"

class Saving_the_file:
    def __init__(self, input_file):
        self.input_file=input_file
        self.home = str(Path.home())
        self.create_destination_folder()


    def save(self):
        output_array=self.input_file.split("/")
        filename=output_array[len(output_array)-1].split(".")[0]
        destination = f"{self.home}/Music/Em Audio extractor"
        return [filename,destination]

    def create_destination_folder(self):
        if not os.path.exists(f"{self.home}/Music/Em Audio extractor"):
            os.makedirs(f"{self.home}/Music/Em Audio extractor")


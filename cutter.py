from moviepy.video.io.VideoFileClip import VideoFileClip



class Cutter:
    def __init__(self, start_time,end_time) -> None:
        self.video = VideoFileClip("vid.mkv")
        self.start_time = start_time
        self.end_time = start_time
        clip = self.video.subclip(start_time, end_time)
        clip.write_videofile("output.mp4")
    
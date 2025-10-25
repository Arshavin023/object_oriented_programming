from abc import ABC, abstractmethod

# # Bad Example: Incompatible interfaces without an adapter.
# class Video:
#     def play(self):
#         print(f"Playing video..")
#     def stop(self):
#         print(f"Stopping video..")

# class Color(ABC):
#     @abstractmethod
#     def apply(self, video: Video):
#         pass

# class BlackAndWhite(Color):
#     def apply(self, video: Video):
#         print("Applying black and white filter to the video.")

# class MidnightColor(Color):
#     def apply(self, video: Video):
#         print("Applying midnight color filter to the video.")

# class VideoEditor:
#     def __init__(self, video: Video):
#         self.video = video

#     def apply_color(self, color: Color):
#         self.video.play()
#         color.apply(self.video)
#         self.video.stop()

# video = Video()
# blackwhite_filter = BlackAndWhite()
# video_editor = VideoEditor(video)
# video_editor.apply_color(blackwhite_filter)



# Good Example: Incompatible interfaces with an adapter.
class Video:
    def play(self):
        print(f"Playing video..")
    def stop(self):
        print(f"Stopping video..")

# 3rd-party Rainbow class that we cannot modify
class Rainbow:
    def setup(self):
        print("Applying rainbow color filter to the video.")
    def update_video(self, video: Video):
        print("Updating video with rainbow effect.")

class Color(ABC):
    @abstractmethod
    def apply(self, video: Video):
        pass

class RainbowColor(Color):
    def __init__(self, rainbow: Rainbow) -> None:
        self.__rainbow = rainbow
    
    def apply(self, video: Video):
        self.__rainbow.setup()
        self.__rainbow.update_video(video)

class BlackAndWhite(Color):
    def apply(self, video: Video):
        print("Applying black and white filter to the video.")

class MidnightColor(Color):
    def apply(self, video: Video):
        print("Applying midnight color filter to the video.")

class VideoEditor:
    def __init__(self, video: Video):
        self.video = video

    def apply_color(self, color: Color):
        self.video.play()
        color.apply(self.video)
        self.video.stop()

video = Video()
video_editor = VideoEditor(video)
video_editor.apply_color(BlackAndWhite())
video_editor.apply_color(MidnightColor())
video_editor.apply_color(RainbowColor(Rainbow()))
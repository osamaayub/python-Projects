from imageio.core.util import Image
from moviepy.editor import *


# convert an video of mp4 format into gif
video = VideoFileClip("title.mp4 ")
video.write_gif("final.gif")

# convert an image into mp4 format using moviepy
file = ["1.png", "2.png", "3.png", "4.png"]
image = ImageSequenceClip(file, fps=2)
image.write_videofile("sofware.mp4", fps=30)

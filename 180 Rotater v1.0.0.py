'''
The PyMovie video editing software would not have been possible without the open-source module MoviePy, along with NumPy, Decorator, tqdm,
PyGame, and ImageMagick modules. Pls make sure that you have installed these modules.

First, download Python 3.10.1 from python.org
Then, install VSCode from: https://code.visualstudio.com/
Then, open this file.
Open the terminal in this file using VSCode.
Next, install MoviePy(which automatically installs NumPy, Decorator, and tqdm.) by typing "pip install moviepy" in the terminal.
Next, install PyGame by typing "pip install pygame" in the terminal.
Next, install ImageMagick from: https://imagemagick.org/script/download.php
ImageMagick is optional as it will only be used if you want to add text to your videos.
'''

#The PyMovie video editing software is a suite of video editing tools.

#The PyMovie video editing software supports almost all the video and audio formats

#Author: Devaansh Dudeja
#Date: 20/12/21
#Location, 2848, Sector-49, Faridabad, Haryana, India, Earth

from moviepy.editor import *
# 180 Rotater v1.0.0 loads the clip, rotates it 180 degrees, and displays it.
# 180 Rotater v1.0.0 also changes the display size to 280.
clip = VideoFileClip("").rotate(180)
clip.ipython_display(width=280)

#To use 180 Rotater, just type the name of your video file in between the double quotes in the VideoFileClip thing on line 11.

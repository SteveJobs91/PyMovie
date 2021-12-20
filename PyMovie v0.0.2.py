'''
The PyMovie video editing software would not have been possible without the open-source module MoviePy, along with NumPy, Decorator, tqdm,
PyGame, and ImageMagick modules. Pls make sure that you have installed these modules.


How to install them:

First, download Python 3.10.1 from python.org
Then, install VSCode from: https://code.visualstudio.com/
Then, open this file.
Open the terminal in this file using VSCode.
Next, install MoviePy(which automatically installs NumPy, Decorator, and tqdm.) by typing "pip install moviepy" in the terminal.
Next, install PyGame by typing "pip install pygame" in the terminal.
Next, install ImageMagick from: https://imagemagick.org/script/download.php
'''

#The PyMovie video editing software is a suite of video editing tools.

#The PyMovie video editing software supports almost all the video and audio formats

#Author: Devaansh Dudeja
#Date: 20/12/21
#Location, 2848, Sector-49, Faridabad, Haryana, India, Earth

# Import everything needed to edit video clips
from moviepy.editor import *
  
# Loading the video
# Enter the name of the video in the below quatoation marks.
clip = VideoFileClip("")
   
# Clipping of the video 
# Getting video for only starting 10 seconds.

'''
You can get the video to start for how much time you want by typing the second the video should start in the place of 0 and the second the 
video should end in the place of 10.
'''

clip = clip.subclip(0, 10)
  
# Rotating video by 180 degrees
# You can change the number of degrees.
clip = clip.rotate(180) 
  
# Reduce the audio volume (volume x 0.5)
#You can also change the volume.
clip = clip.volumex(0.5)
  
# Display
# You can also change the width.
clip.ipython_display(width = 280)


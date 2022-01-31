# Embed-subtitle-into-mp4-using-python-and-FFmpeg

You need to install

1. python 3.7 or above version and
2. ffmpeg
   Into your local machine.

Make sure the file names does not conatin single quotation.
mp4 file and subtitle files(.srt) should have similar name.

all the mp4 files and subtitle files(.srt) should contain a single folder
Sometimes the file name length can be affected not to work properly. This might be an issue but for me it wasn't.
once you create the environment for running the script you can follow the below steps to generate the output videos

1. Download the scipt.py from this repo
2. Copy and paste the script.py inside the folder where the .mp4 video files and .srt subtitle files located
3. Open the command prompt in any way and navigate to the relevent folder. (Shortcuts - once you are inside the folder press windows+L. Then hit enter.)
4. Type and run "python script.py"
5. Then it will start to save the output videos to a new folder called 'output_videos'. This process will take considerable time depending on the video size and performance of the machine.

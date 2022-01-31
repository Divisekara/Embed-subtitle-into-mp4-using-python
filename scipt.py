import imp
import os
import subprocess

def printing(file_list):
    for i in file_list:
        print(i)

file_list = os.listdir()
# print(file_list)

video_file_names = []

for i in file_list:
    if(".mp4" in i):
        video_file_names.append(i.replace(".mp4",""))

for j in video_file_names:
    input_video = j + '.mp4'
    input_sub = j + ".srt"
    output_video = j + "_srt_" + ".mp4"
    command = "ffmpeg -i {} -i {} -c:s mov_txt -c:v copy -c:a copy {}".format(input_video, input_sub, output_video)
    try:
        subprocess.run(command)
    except:
        print(j)
        continue

# printing(video_file_names)

# command = "ffmpeg -i {} -i {} -c:s mov_txt -c:v copy -c:a copy {}".format(input_video, input_sub, output_video)
# subprocess.run()


# "ffmpeg -i inputfile.mp4 -i subtitles.srt -c:s mov_text -c:v copy -c:a copy outputfile.mp4"


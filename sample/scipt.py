
import os
import subprocess

def printing(file_list):
    for i in file_list:
        print(i)

path = "C:/Users/Asitha/Desktop/copy/sample/"
path2 = "C:\\Users\\Asitha\\Desktop\\copy\\sample\\"

file_list = os.listdir(path)
# print(file_list)

video_file_names = []

for i in file_list:
    if(".mp4" in i):
        video_file_names.append(i.replace(".mp4",""))

printing(video_file_names)

for j in video_file_names:
    input_video =path2 + j + '.mp4'
    input_sub = j + ".srt"
    output_video = j + "_srt_" + ".mp4"
    
    # command = "ffmpeg -i {} -i {} -c:s mov_txt -c:v copy -c:a copy {}".format(input_video, input_sub, output_video)
    command = "ffmpeg -i {} -vf subtitles={} {}".format(input_video, input_sub, output_video)
    print(command)
    subprocess.run(command, shell=True)
    # os.system(command)
  
"ffmpeg -i 1.mp4 -i 1.srt -c:s mov_txt -c:v copy -c:a copy 1_srt_.mp4"
"ffmpeg -i 1.mp4 -vf subtitles=1.srt 1_srt.mp4"
import os
import subprocess

def printing(file_list):
    for i in file_list:
        print(i)

file_list = os.listdir(".")


video_file_names = []

for i in file_list:
    if(".mp4" in i):
        video_file_names.append(i.replace(".mp4",""))

printing(video_file_names)

for j in video_file_names:
    input_video = j + '.mp4'
    input_sub = j + ".srt"
    output_video = j + "_srt_" + ".mp4"
    
    command = 'ffmpeg -i "{}" -vf subtitles="{}" "{}" '.format(input_video, input_sub, output_video)
    try:
        subprocess.run(command, shell=True)
    except:
        continue

print(command)

# ffmpeg -i "D:\\sample folder\\input video.mp4" -vf subtitles="D:\\sample folder\\input video.srt" "D:\\sample folder\\output video.mp4" 
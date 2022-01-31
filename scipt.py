
import os
import subprocess

def printing(file_list):
    for i in file_list:
        print(i)

path = "C:/Users/Asitha/Desktop/copy/"
path2 = "C:\\Users\\Asitha\\Desktop\\copy\\"

file_list = os.listdir(path)


video_file_names = []

for i in file_list:
    if(".mp4" in i):
        video_file_names.append(i.replace(".mp4",""))

printing(video_file_names)

for j in video_file_names:
    input_video =path2 + j + '.mp4'
    input_sub = j + ".srt"
    output_video = j + "_srt_" + ".mp4"
    
    command = 'ffmpeg -i "{}" -vf subtitles="{}" "{}" '.format(input_video, input_sub, output_video)
    subprocess.run(command, shell=True)

print(command)


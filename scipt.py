import os
import subprocess

file_list = os.listdir(".")
subprocess.run('mkdir output_videos', shell=True)

video_file_names = []

for i in file_list:
    if(".mp4" in i):
        video_file_names.append(i.replace(".mp4",""))

for j in video_file_names:
    input_video = j + '.mp4'
    input_sub = j + ".srt"
    output_video = ".\\output_videos\\" + j + "_srt_" + ".mp4"
    
    command = 'ffmpeg -i "{}" -vf subtitles="{}" "{}" '.format(input_video, input_sub, output_video)
    try:
        subprocess.run(command, shell=True)
    except:
        continue
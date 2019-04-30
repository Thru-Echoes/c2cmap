import os
import subprocess

def get_video_to_frames_shell(input_path, output_path, fps=30):
    ##return "ffmpeg -i ../videodata/" + input_path + " -vf fps=" + str(fps) + " -q:v 1 ../imagedata/" + output_path + "/frame_%09d.jpg"
    return ["ffmpeg",
           "-i",
           "videodata/" + input_path,
           "-vf",
           "fps=" + str(fps),
           "-q:v",
           "1",
           "imagedata/" + output_path + "/frame_%09d.jpg"]


## Example use: sample 1 frame every 10 seconds from nest13B35A, on 01-August, video 00006.MTS 
#shell_00006 = get_video_to_frames_shell("13B35A/0801_0841/00006.MTS", "13B35A/0801_0841/00006", 1)
#subprocess.run(shell_00006)
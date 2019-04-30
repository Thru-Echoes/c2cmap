import os
import subprocess

def get_video_to_frames_shell(input_path, start_time, end_time, output_path, fps=30):
    ##return "ffmpeg -i " + input_path + " -vf fps=" + str(fps) + " -q:v 1 " + output_path + "/frame_%09d.jpg"
    return ["ffmpeg",
            "-loglevel",
            "verbose",
            "-ss",
            start_time,
            "-to",
            end_time
           "-i",
           input_path,
           "-vf",
           "fps=" + str(fps),
           "-q:v",
           "1",
           output_path + "/frame_%09d.jpg"]


## Example use: sample 1 frame every 10 seconds from nest13B35A, on 01-August, video 00006.MTS 
## - for exactly 1 min between 1min 21.5sec to 2min 21.5sec 
## 
## Oliver example 
#shell_00006 = get_video_to_frames_shell("videodata/13B35A/0801_0841/00006.MTS", 00:01:21.500, 00:02:21.500, "imagedata/13B35A/0801_0841/00006", 1)
#subprocess.run(shell_00006)

## Mad Mike's example
shell_command = get_video_to_frames_shell(input_path = "E:\20190327", 
                                          start_time = "00:00:00.000", 
                                          end_time = "00:05:00.000", 
                                          output_path = "E:\20190327\Frames",
                                          fps = 60)
subprocess.run(shell_command)
import os
import random
import time
from subprocess import PIPE, Popen, STDOUT

directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'videos')

videos = []


def get_videos():
    global videos
    videos = []
    for file in os.listdir(directory):
        if file.lower().endswith('.mp4'):
            videos.append(os.path.join(directory, file))


def play_videos():
    global videos
    if len(videos) == 0:
        get_videos()
        time.sleep(5)
        return
    random.shuffle(videos)
    for video in videos:
        play_process = Popen(['cvlc', '--fullscreen', '--no-osd', '--aspect-ratio', '16:9', video], stdout=PIPE, stderr=STDOUT)
        play_process.wait()


while True:
    play_videos()


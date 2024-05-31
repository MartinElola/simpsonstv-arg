import os
import random
import time
from subprocess import Popen, PIPE, STDOUT

# Ruta completa al directorio de videos
directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'videos')

videos = []

def get_videos():
    global videos
    videos = []
    print(f"Buscando videos en {directory}")
    if not os.path.exists(directory):
        print(f"El directorio base {directory} no existe.")
        return

    for file in os.listdir(directory):
        if file.lower().endswith('.mp4'):
            videos.append(os.path.join(directory, file))
            print(f"Agregado: {os.path.join(directory, file)}")
    
    if not videos:
        print("No se encontraron videos")

def play_videos():
    global videos
    if len(videos) == 0:
        get_videos()
        if len(videos) == 0:  # Añadido para evitar un bucle infinito en caso de que no se encuentren videos
            print("No se encontraron videos para reproducir.")
            time.sleep(10)
            return
    random.shuffle(videos)
    for video in videos:
        print(f"Reproduciendo: {video}")
        play_process = Popen(['sudo', 'mplayer', '-vo', 'fbdev2', '-vf', 'scale=480:360', video], stdout=PIPE, stderr=STDOUT)
        play_process.communicate()  # Asegura que el proceso de reproducción espera hasta que el video termine

while True:
    play_videos()
    time.sleep(5)  # Espera un poco antes de comenzar de nuevo

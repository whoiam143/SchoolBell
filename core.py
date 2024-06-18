import time
import simpleaudio as sa
from threading import Thread
import datetime

from data.db import get_all_time, get_path_to_music


def timer():
    print("next reg")
    time_lst = get_all_time()
    current_time = str(datetime.datetime.now().time())[:5]
    while current_time not in time_lst:
        time.sleep(30)
        timer()
    else:
        play_song(current_time)


def play_song(timex):
    path = list(get_path_to_music(timex))[0][0]
    wave_obj = sa.WaveObject.from_wave_file(path)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    time.sleep(30)
    timer()


def main_thread():
    thread = Thread(target=timer)
    thread.start()
    return thread

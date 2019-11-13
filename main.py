from playlist import create_play_list
from interface import create_interface
from wavemusic import play_music

M_LIST = 1
M_STOP_PLAY = 2
M_SUBS = 3
M_PLOT = 4
M_EXIT = 9


if __name__ == "__main__":
    play_list = create_play_list()
    interface = create_interface(play_list.musics)
    interface.start()
    interface.load()
    cod_music = interface.list()
    cod_function = play_music()

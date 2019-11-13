from const import M_LIST, M_EXIT, M_PLOT, M_SUBS, M_STOP_PLAY
from playlist import create_play_list
from interface import create_interface
from wavemusic import plot_chart

if __name__ == "__main__":
    play_list = create_play_list()
    interface = create_interface(play_list.musics)
    interface.start()
    interface.load()
    while True:
        cod_music = interface.list()
        if cod_music != M_EXIT:
            while True:
                cod_function = interface.options()
                if cod_function == M_LIST:
                    break
                elif cod_function == M_STOP_PLAY:
                    pass
                elif cod_function == M_SUBS:
                    pass
                elif cod_function == M_PLOT:
                    plot_chart(play_list.musics[cod_music][0])
                elif cod_function == M_EXIT:
                    exit()
        else:
            exit()

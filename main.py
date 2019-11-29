from const import M_LIST, M_EXIT, M_PLOT, M_SUBS, M_STOP_PLAY
from playlist import create_play_list
from interface import create_interface
from wavemusic import plot_chart, create_music

if __name__ == "__main__":
    play_list = create_play_list()
    interface = create_interface(play_list.musics)
    interface.clean()
    interface.start()
    interface.load()
    while True:
        cod_music = interface.list()  # lista músicas
        if cod_music != M_EXIT:
            control = None
            tocando = False
            while True:
                cod_function = interface.options()  # lista funcionalidades
                if cod_function == M_LIST:  # retorna para a listagem de músicas
                    if control is not None:
                        control.stop()
                    break
                elif cod_function == M_STOP_PLAY:  # toca ou para a música
                    if not tocando:
                        cod_speed = interface.speed()
                        control = create_music(play_list.musics[cod_music][0], cod_speed)
                        control.play()
                        tocando = True
                    else:
                        control.stop()
                        tocando = False
                elif cod_function == M_SUBS:  # mostra legenda
                    interface.clean()
                    play_list.show_sub(cod_music)
                    stop = input()
                elif cod_function == M_PLOT:
                    plot_chart(play_list.musics[cod_music][1])
                elif cod_function == M_EXIT:  # sai do programa
                    if control is not None:
                        control.stop()
                    exit()
        else:
            exit()

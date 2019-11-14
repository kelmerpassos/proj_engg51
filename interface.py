import time
from const import M_EXIT
import os


class Interface:
    def __init__(self, musics):
        super(Interface, self).__init__()
        self.playlist = {key: value[1][6:-4] for key, value in musics.items()}

    def options(self):
        option = input('''
        1 - TROCAR MÚSICA
        2 - PARAR/TOCAR MÚSICA
        3 - MOSTRAR LETRA
        4 - PLOTAR GRÁFICO
        0 - FECHAR PROGRAMA
        ''')
        while True:
            if option in ('1', '2', '3', '4', '0'):
                return option
            else:
                print('cls')
                print('Código inválido, digite novamente!')

    def list(self):
        print('MÚSICAS:', end='\n\n\n')
        for key, value in self.playlist.items():
            print(str(key)+' - '+value, end='\n\n')
        print('0 - FECHAR PROGRAMA')
        while True:
            option = input('Digite o número da música.')
            try:
                option = int(option)
            except ValueError:
                option = -1
            if option in self.playlist.keys() or option == M_EXIT:
                return option
            else:
                os.system('cls')
                print('Código inválido, digite novamente!')

    def start(self):
        print('''
        _____________________________________
                    PLAYLIST ENNG51 
        _____________________________________
    
                 ALUNOS: KELMER & MAIKE
                 
            ''')
        time.sleep(2)

    def load(self):
        print('Carregando...')
        time.sleep(3)
        os.system('cls')


def create_interface(musics):
    interface = Interface(musics)
    return interface


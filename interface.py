import time
from const import M_EXIT
import os


class Interface:
    def __init__(self, musics):
        super(Interface, self).__init__()
        self.playlist = {key: value[0][6:-4] for key, value in musics.items()}  # salva lista de músicas

    def clean(self):
        if os.name == 'nt':
            os.system('cls')
        elif os.name == 'posix':
            os.system('clear')

    def options(self):
        while True:
            self.clean()
            print('1 - TROCAR MÚSICA')
            print('2 - PARAR/TOCAR MÚSICA')
            print('3 - MOSTRAR LETRA')
            print('4 - PLOTAR GRÁFICO')
            print('0 - FECHAR PROGRAMA')
            option = input()
            if option in ('1', '2', '3', '4', '0'):
                return int(option)
            else:
                self.clean()
                print('Código inválido, digite novamente!')
                time.sleep(2)

    def speed(self):
        while True:
            self.clean()
            print('Nível de velocidade')
            print('1 - Velocidade normal')
            print('2 - Velocidade um')
            print('3 - Velocidade um')
            print('4 - Velocidade três')
            option = input()
            if option in ('1', '2', '3', '4'):
                return int(option)
            else:
                self.clean()
                print('Código inválido, digite novamente!')
                time.sleep(2)

    def list(self):
        while True:
            self.clean()
            print('MÚSICAS:', end='\n\n')
            for key, value in self.playlist.items():
                print(str(key) + ' - ' + value)
            print('0 - FECHAR PROGRAMA', end='\n\n')
            print('Digite o número da música.')
            option = input()
            try:
                option = int(option)
            except ValueError:
                option = -1
            if option in self.playlist.keys() or option == M_EXIT:
                return option
            else:
                self.clean()
                print('Código inválido, digite novamente!')
                time.sleep(2)

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
        self.clean()


def create_interface(musics):
    interface = Interface(musics)
    return interface


import os


class PlayList:
    musics = {}
    count = 0
    path = 'music'

    def __init__(self):
        super(PlayList, self).__init__()
        paths = [os.path.join(self.path, name) for name in os.listdir(self.path)]  # carrega todos os arquivos
        self.all_files = [arq for arq in paths if  # filtra apenas os arquivos .wav e .txt
                          os.path.isfile(arq) and (arq.lower().endswith('.wav') or arq.lower().endswith('.txt'))]
        self.index()  # chama função de indexar músicas

    def index(self):
        for file in self.all_files:
            file_plot = self.valid_plot(file)  # chama função para verificar se existe arquivo de plotagem
            file_sub = self.valid_sub(file)  # chama função para verificar se exite arquivo de legenda
            if file_plot is not None and file_sub is not None:
                self.count = self.count + 1
                file = self.path + '/' + file[6:]
                file_sub = self.path + '/' + file[6:-4] + '-Sub.txt'
                self.musics[self.count] = [file, file_plot, file_sub]  # salvo arquivos em uma lista

    def valid_plot(self, file):
        file_plot_name = file[:-4] + '-Plot.wav'
        if file_plot_name in self.all_files:  # verifica se o arquivo se encontra na lista com todos os arquivos
            return file_plot_name
        return None

    def valid_sub(self, file):
        file_sub_name = file[:-4] + '-Sub.txt'
        if file_sub_name in self.all_files:  # verifica se o arquivo se encontra na lista com todos os arquivos
            return file_sub_name
        return None

    def show_sub(self, index):
        arq = open(self.musics[index][2], 'r')  # abre arquivo em modo leitura
        print(arq.read())  # ler arquivo


def create_play_list():
    playlist = PlayList()
    return playlist

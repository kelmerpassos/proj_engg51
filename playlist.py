import os


class PlayList:
    musics = {}
    count = 0
    path = 'music'

    def __init__(self):
        super(PlayList, self).__init__()
        paths = [os.path.join(self.path, name) for name in os.listdir(self.path)]
        self.all_files = [arq for arq in paths if os.path.isfile(arq) and (arq.lower().endswith('.wav') or arq.lower().endswith('.txt'))]
        self.index()

    def index(self):
        for file in self.all_files:
            file_plot = self.valid_plot(file)
            file_sub = self.valid_sub(file)
            if file_plot is not None and file_sub is not None:
                self.count = self.count+1
                file = self.path+'/'+file[6:]
                file_sub = self.path + '/' + file[6:-4] + '-Sub.txt'
                self.musics[self.count] = [file, file_plot, file_sub]

    def valid_plot(self, file):
        file_plot_name = file[:-4]+'-Plot.wav'
        if file_plot_name in self.all_files:
            return file_plot_name
        return None

    def valid_sub(self, file):
        file_sub_name = file[:-4]+'-Sub.txt'
        if file_sub_name in self.all_files:
            return file_sub_name
        return None

    def show_sub(self, index):
        arq = open(self.musics[index][2], 'r')
        print(arq.read())


def create_play_list():
    playlist = PlayList()
    return playlist

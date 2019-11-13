import os


class PlayList:
    musics = {}
    count = 0
    path = 'music'

    def __init__(self):
        super(PlayList, self).__init__()
        paths = [os.path.join(self.path, name) for name in os.listdir(self.path)]
        self.all_files = [arq for arq in paths if os.path.isfile(arq) and arq.lower().endswith('.wav')]
        self.index()

    def index(self):
        for file in self.all_files:
            file_plot = self.valid_plot(file)
            if file_plot is not None:
                self.count = self.count+1
                self.musics[self.count] = [file, file_plot]

    def valid_plot(self, file):
        file_plot_name = file[:-4]+'-Plot.wav'
        if file_plot_name in self.all_files:
            return file_plot_name
        return None


def create_play_list():
    playlist = PlayList()
    return playlist

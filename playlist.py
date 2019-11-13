import os


class PlayList:
    musics = {}
    count = 0

    def __int__(self, teste):
        super(PlayList, self).__init__()
        self.path = 'music'
        paths = [os.path.join(self.path, name) for name in os.listdir(self.path)]
        self.all_files = [arq for arq in paths if os.path.isfile(arq) and arq.lower().endswith('.wav')]

    def index(self):
        for file in self.all_files:
            if not file.lower().endswith('-Plot.wav'):
                file_plot = self.get_file_plot(file)
                if file_plot is not None:
                    self.count += self.count
                    self.musics[self.count] = [file, self.get_file_plot(file)]

    def get_file_plot(self, file):
        file_plot_name = {file[:-4]}+'-Plot.wav'
        if file_plot_name in self.all_files:
            return file_plot_name
        return None


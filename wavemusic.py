import pyaudio
import os
import wave
import threading
import numpy
import soundfile
from matplotlib import pyplot


class WaveSignal:
    def __init__(self, key, music):
        self.index = key
        self.music = music
        super(WaveSignal, self).__init__()
        self.signal, self.samplingrate = soundfile.read(music)

    def convert_time(self):
        period = 1 / self.samplingrate
        return numpy.arange(0, len(self.signal) * period, period)

    def plot_chart(self):
        pyplot.plot(self.convert_time(), self.signal)
        pyplot.title('Gráfico do Sinal')
        pyplot.xlabel('tempo (s)')
        pyplot.ylabel('amplitude (V)')
        pyplot.grid()
        pyplot.show()


class WavePlayer(threading.Thread):
    def __init__(self, filepath, loop=True):
        super(WavePlayer, self).__init__()
        self.filepath = os.path.abspath(filepath)
        self.loop = loop

    def run(self):
        CHUNKSIZE = 2048
        wf = wave.open(self.filepath, 'r')
        player = pyaudio.PyAudio()
        stream = player.open(
            format=player.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True
        )
        data = wf.readframes(CHUNKSIZE)
        while self.loop:
            stream.write(data)
            data = wf.readframes(CHUNKSIZE)
            if data == b'':
                self.stop()
        stream.close()
        player.terminate()

    def play(self):
        self.start()

    def stop(self):
        self.loop = False


def play_music(key, music):
    player = WavePlayer(key, music)
    player.play()
    return player


def plot_chart(music):
    grafic = WaveSignal(music)
    grafic.plot_chart()




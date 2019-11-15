import pyaudio
import os
import wave
import threading
import numpy
import soundfile
from matplotlib import pyplot


class WaveSignal:
    def __init__(self, music):
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
    def __init__(self, filepath, speed, loop=True):
        super(WavePlayer, self).__init__()
        self.filepath = os.path.abspath(filepath)
        self.loop = loop
        self.speed = speed

    def run(self):
        CHUNKSIZE = 2048
        wf = wave.open(self.filepath, 'rb')
        player = pyaudio.PyAudio()
        stream = player.open(
            format=player.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate()*self.speed,
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


def create_music(music, speed):
    player = WavePlayer(music, speed)
    return player


def plot_chart(music):
    grafic = WaveSignal(music)
    grafic.plot_chart()




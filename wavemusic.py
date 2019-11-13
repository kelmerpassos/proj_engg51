import pyaudio
import os
import wave
import threading


class WavePlayerLoop(threading.Thread):
    def __init__(self, filepath, loop=True):
        super(WavePlayerLoop, self).__init__()
        self.filepath = os.path.abspath(filepath)
        self.loop = loop

    def run(self):
        CHUNKSIZE = 2048
        wf = wave.open(self.filepath, 'rb')
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


def play_music(music):
    player = WavePlayerLoop(music)
    player.play()
    return player




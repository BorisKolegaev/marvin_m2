import pyaudio
import vosk
import os


class SpeechRecognitionService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.sample_rate = 16000
            cls._instance.mic = pyaudio.PyAudio()
            #cls._instance.model_path = os.path.dirname(os.getcwd()) + "\\resources\\vosk_model"
            cls._instance.model_path = 'D:\Projects\PyCharmWorkspace\marvin_m2\\resources\\vosk_model'
            cls._instance.model = vosk.Model(cls._instance.model_path)
            cls._instance.kaldi_rec = vosk.KaldiRecognizer(cls._instance.model, cls._instance.sample_rate)
        return cls._instance

    def get_command(self):
        listen = True
        stream = self.mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True)
        while listen:
            listen = True
            stream.start_stream()
            try:
                data = stream.read(4096)
                if self.kaldi_rec.AcceptWaveform(data):
                    result = self.kaldi_rec.Result()
                    response = result[14:-3]
                    listen = False
                    stream.close()
                    return response
            except OSError:
                pass


if __name__ == "__main__":
    speech_recognizer = SpeechRecognitionService()
    command = speech_recognizer.get_command()
    print(command)

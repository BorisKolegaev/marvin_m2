import torch
import os
import sounddevice
import time


class TtsService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TtsService, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        device = torch.device('cpu')
        torch.set_num_threads(4)
        #local_file = 'D:\Programs\PycharmProject\marvin_m2\services\model.pt'
        local_file = os.path.join(os.getcwd(), os.path.join('services', 'model.pt'))

        self.model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
        self.model.to(device)

        self.sample_rate = 48000
        self.speaker = 'kseniya'
        self.put_accent = True
        self.put_yo = True

    def generate_audio(self, text):
        audio = self.model.apply_tts(text=text,
                                     speaker=self.speaker,
                                     sample_rate=self.sample_rate,
                                     put_accent=self.put_accent,
                                     put_yo=self.put_yo)
        return audio

    def play_audio(self, audio):
        sounddevice.play(audio, self.sample_rate)
        time.sleep(len(audio) / self.sample_rate + 0.1)
        sounddevice.stop()

# Usage
# tts_singleton = TtsService()
# audio_data = tts_singleton.generate_audio('тест')
# tts_singleton.play_audio(audio_data)

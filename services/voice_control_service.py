import eel
from services.open_ai_service import OpenAiService
from services.speech_recognition_service import SpeechRecognitionService
from services.wake_word_service import WakeWordService
from services.expert_system_service import ExpertSystemService
from services.tts_service import TtsService


class VoiceControlService:

    def __init__(self):
        self.running = True
        self.wws = WakeWordService()
        self.ess = ExpertSystemService()
        self.srs = SpeechRecognitionService()
        self.tts = TtsService()

    def start_voice_control(self):
        while self.running:
            status = self.wws.start_wake_detection()
            if status == "Detected":

                eel.pulse()
                command = self.srs.get_command()
                print(command)
                eel.stop_pulse()
                eel.spin()
                reply = self.ess.work(command)
                eel.stop_spin()
                print(reply)
                #eel.toggleAnimation()
                audio_data = self.tts.generate_audio(reply)
                self.tts.play_audio(audio_data)

    def stop_voice_control(self):
        self.running = False


if __name__ == "__main__":
    wake_word = VoiceControlService()
    wake_word.start_voice_control()

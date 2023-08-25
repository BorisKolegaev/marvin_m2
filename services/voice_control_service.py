import eel
from services.open_ai_service import OpenAiService
from services.speech_recognition_service import SpeechRecognitionService
from services.wake_word_service import WakeWordService
from services.expert_system_service import ExpertSystemService


class VoiceControlService:

    def __init__(self):
        self.running = True
        self.wws = WakeWordService()
        self.ess = ExpertSystemService()
        self.srs = SpeechRecognitionService()

    def start_voice_control(self):
        while self.running:
            status = self.wws.start_wake_detection()
            if status == "Detected":

                eel.pulse()
                command = self.srs.get_command()
                eel.spin()
                reply = self.ess.work(command)
                print(reply)
                #eel.toggleAnimation()

    def stop_voice_control(self):
        self.running = False


if __name__ == "__main__":
    wake_word = VoiceControlService()
    wake_word.start_voice_control()

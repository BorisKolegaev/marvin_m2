import pvporcupine
from pvrecorder import PvRecorder
import os


class WakeWordService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.current_path = os.getcwd()
            cls._instance.parent_dir = os.path.dirname(cls._instance.current_path)
            cls._instance.access_key = "gbq2u+SsOfhJBDK7YZk04WhkvdvzgGRWX5/Os58oSAtJT3sxT/bTiQ=="
            cls._instance.porcupine = pvporcupine.create(
                access_key=cls._instance.access_key, keywords=['computer']
            )
            cls._instance.recorder = PvRecorder(
                device_index=-1, frame_length=cls._instance.porcupine.frame_length
            )
            cls._instance.is_detection_active = False

        return cls._instance

    def start_wake_detection(self):
        if self.is_detection_active:
            print("Detection loop is already active.")
            return
        try:
            self.is_detection_active = True
            self.recorder.start()
            while self.is_detection_active:
                keyword_index = self.porcupine.process(self.recorder.read())
                if keyword_index >= 0:
                    print("Detected")
                    self.stop_wake_detection()
                    return "Detected"

        except KeyboardInterrupt:
            self.stop_detection()
        # finally:
        #     self.porcupine.delete()
        #     self.recorder.delete()

    def stop_wake_detection(self):
        self.is_detection_active = False
        self.recorder.stop()


if __name__ == "__main__":
    wake_word = WakeWordService()
    wake_word.start_wake_detection()

from __future__ import annotations
from abc import abstractmethod, ABC

"""
consider an app for music composition.
The app has a audio control board with buttons like
play, pause, record and stop, and each has different
action upon the click event.
"""


# Receiver
class AudioIODeviceController:
    def play(self, name) -> None:
        print(f'AudioIODeviceController: playing {name}')

    def pause(self, name) -> None:
        print(f'AudioIODeviceController: pausing {name}')

    def record(self, name) -> None:
        print(f'AudioIODeviceController: recording {name}')

    def stop(self, name) -> None:
        print(f'AudioIODeviceController: stopping {name}')

    def save(self, name: str) -> None:
        print(f'AudioIODeviceController: saving {name}')

    def turn_on_microphone(self) -> None:
        print('AudioIODeviceController: turning on microphone')


# Command
class AudioCommand(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


# Simple Command
class PrintAudioInfoCommand(AudioCommand):
    def __init__(self, audio: str):
        self._audio = audio

    def execute(self) -> None:
        print(f'PrintAudioInfoCommand: {self._audio}')


# Complex Command
class RecordAudioCommand(AudioCommand):
    def __init__(
            self,
            io_controller: AudioIODeviceController,
            project_name: str
            ) -> None:
        self._io_controller = io_controller
        self._project_name = project_name

    def execute(self) -> None:
        print('RecordAudioCommand: sending request to IO Controller')
        self._io_controller.turn_on_microphone()
        self._io_controller.record(self._project_name)
        self._io_controller.save(self._project_name)


class RecordAudioBoard:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: AudioCommand) -> None:
        self._on_start = command

    def set_on_finish(self, command: AudioCommand) -> None:
        self._on_finish = command

    def record_audio(self) -> None:
        print('AudioBoard: start recording audio')
        if isinstance(self._on_start, AudioCommand):
            self._on_start.execute()

        print('AudioBoard: finished recording audio')
        if isinstance(self._on_finish, AudioCommand):
            self._on_finish.execute()


if __name__ == "__main__":
    record_audio_board = RecordAudioBoard()
    io_controller = AudioIODeviceController()

    record_audio_board.set_on_start(
        RecordAudioCommand(io_controller, 'my_project')
    )

    record_audio_board.set_on_finish(
        PrintAudioInfoCommand('my_project')
    )

    record_audio_board.record_audio()

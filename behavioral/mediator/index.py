from __future__ import annotations
from abc import ABC

"""
consider an app for music composition.
The app has a lot of different components like a list
of tracks and a audio editing tool. All these components
has a visual representation and they need to iteract with
each other in a corrdinated way.
"""


# Component
class Component(ABC):
    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


# Concrete Component
class TrackList(Component):
    def select_track(self) -> None:
        print('TrackList: track selected')
        self.mediator.notify(self, 'track_selected')

    def save_track(self) -> None:
        print('TrackList: save track')
        self.mediator.notify(self, 'save_track')


# Concrete Component
class AudioEditor(Component):
    def open_track(self) -> None:
        print('AudioEditor: open track on editor')
        self.mediator.notify(self, 'open_track')

    def add_effects(self) -> None:
        print('AudioEditor: adding effects')
        self.mediator.notify(self, 'add_effects')

    def save_as_copy(self) -> None:
        print('AudioEditor: save track as copy')
        self.mediator.notify(self, 'save_as_copy')


# Mediator
class Mediator(ABC):
    def notify(self, sender: object, event: str) -> None:
        pass


# Concrete Mediator
class AudioMediator(Mediator):
    def __init__(
            self,
            track_list: TrackList,
            audio_editor: AudioEditor
            ) -> None:
        self._track_list = track_list
        self._track_list.mediator = self
        self._audio_editor = audio_editor
        self._audio_editor.mediator = self

    def notify(self, sender: object, event: str) -> None:
        print(f'AdioMediator: event {event} received')
        if event == 'track_selected':
            print('AdioMediator: trigger open_track')
            self._audio_editor.open_track()

        elif event == 'save_as_copy':
            print('AdioMediator: trigger save_track')
            self._track_list.save_track()


if __name__ == '__main__':
    track_list = TrackList()
    audio_editor = AudioEditor()
    mediator = AudioMediator(track_list, audio_editor)

    print('Client: trigger select_track')
    track_list.select_track()

    print('\nClient: trigger add_effects')
    audio_editor.add_effects()

    print('\nClient: trigger save_as_copy')
    audio_editor.save_as_copy()

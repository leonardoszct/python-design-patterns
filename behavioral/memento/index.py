from __future__ import annotations
from abc import ABC
from datetime import datetime

"""
consider an app for music composition.
The app allows user to add instrument melodies,
lyrics and effects to a audio track. It needs to
support undo/redo functionality to allow users to
revert changes
"""


# Memento
class Memento(ABC):
    def get_name(self) -> str:
        pass

    def get_date(self) -> str:
        pass


# Concrete Memento
class LyricsMemento(Memento):
    def __init__(self, lyric: str) -> None:
        self._state = lyric
        self._date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def get_state(self) -> str:
        return self._state

    def get_date(self) -> str:
        return self._date

    def get_name(self) -> str:
        return f'{self._date} / ({self._state[:9]}...)'


# Originator
class Lyrics:
    _state = None

    def __init__(self, state: str) -> None:
        self._state = state
        print(f'Lyrics: current state is {self._state}')

    def set_lyrics(self, lyrics: str) -> None:
        print('Lyrics: setting lyrics')
        self._state = f' {lyrics}'
        print(f'Lyrics: new state is {self._state}')

    def save(self) -> LyricsMemento:
        print('Lyrics: saving current state to memento')
        return LyricsMemento(self._state)

    def restore(self, memento: LyricsMemento) -> None:
        self._state = memento.get_state()
        print(f'Lyrics: restoring state to {self._state}')


# Caretaker
class LyricsHistory:
    def __init__(self, lyrics: Lyrics) -> None:
        self._lyrics = lyrics
        self._mementos = []

    def backup(self) -> None:
        print('LyricsHistory: saving lyrics state')
        self._mementos.append(self._lyrics.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f'LyricsHistory: restoring state to {memento.get_name()}')

        try:
            self._lyrics.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print('LyricsHistory: list of lytics mementos:')
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == '__main__':
    print('Creating lyrics...')
    lyrics = Lyrics('Lorem ipsum dolor sit amet')
    history = LyricsHistory(lyrics)

    print()
    history.backup()
    lyrics.set_lyrics('Consectetur adipiscing elit')

    print()
    history.backup()
    lyrics.set_lyrics('Sed do eiusmod tempor incididunt ut labore')

    print()
    history.backup()
    lyrics.set_lyrics('Et dolore magna aliqua')

    print()
    history.show_history()

    print('\nUndoing...')
    history.undo()

    print('\nUndoing...')
    history.undo()

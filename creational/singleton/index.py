from time import sleep

"""
Consider an app that plays instrumental
samples on your device's speakers. It can not
play multiple samples at the same time, so
the app will have only one instance of the player.
"""


# helper class - not part of the pattern
class Sample():
    def __init__(self, name: str, duration: int) -> None:
        self.name = name
        self.duration = duration


# Singleton Meta
class SoundPlayerMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SoundPlayer(metaclass=SoundPlayerMeta):
    play_history = []

    def play_sample(self, sample: Sample) -> None:
        print(f'♪ playing {sample.name} sample - duration: {sample.duration}s')
        sleep(sample.duration)
        self.play_history.append(sample)

    def print_history(self) -> None:
        print('\n♫ Player history:')
        for sample in self.play_history:
            print(f'♪ {sample.name}')


if __name__ == "__main__":
    home_page_player = SoundPlayer()
    liked_page_player = SoundPlayer()
    history_page_player = SoundPlayer()

    print('Created SoundPlayer instance for HOME page')
    print('\nCreated SoundPlayer instance for LIKED page')
    print('\nCreated SoundPlayer instance for HISTORY page')

    home_id = id(home_page_player)
    like_id = id(liked_page_player)
    history_id = id(history_page_player)

    if home_id == like_id == history_id:
        print('\nAll instances have the same id, they are the same')
    else:
        print('\nAll instances have different ids, they are different')

    guitar_sample = Sample('guitar', 2)
    drums_sample = Sample('drums', 2)
    piano_sample = Sample('piano', 3)

    print('\nPlaying samples on HOME page instance:')
    home_page_player.play_sample(guitar_sample)
    home_page_player.play_sample(drums_sample)

    print('\nPlaying samples on LIKED page instance:')
    liked_page_player.play_sample(piano_sample)

    print('\nWhen accessing the player HISTORY page:')
    history_page_player.print_history()

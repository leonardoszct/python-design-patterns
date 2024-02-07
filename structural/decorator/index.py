"""
Consider an app for simulating the sound of musical instruments.
The app has a basic instrument player but it needs to add
players with effects and combine them when playing.
"""


# helper class - not part of the pattern
class Instrument:
    def __init__(self, name: str) -> None:
        self._name = name


# Component
class InstrumentPlayer():
    def __init__(self, instrument: Instrument) -> None:
        self._instrument = instrument

    @property
    def play_sample(self) -> None:
        pass


# Concrete Component
class BasicInstrumentPlayer(InstrumentPlayer):
    def play_sample(self) -> None:
        print(f'♪ playing {self._instrument._name}')


# Decorator
class InstrumentPlayerDecorator(InstrumentPlayer):
    def __init__(self, instrument_player: InstrumentPlayer) -> None:
        self._instrument_player = instrument_player

    @property
    def instrument_player(self) -> InstrumentPlayer:
        return self._instrument_player

    def play_sample(self) -> None:
        return self._instrument_player.play_sample()


# Concrete Decorator A
class EchoDecorator(InstrumentPlayerDecorator):
    def play_sample(self) -> None:
        print('+ adding echo')
        super().play_sample()


# Concrete Decorator B
class DistortionDecorator(InstrumentPlayerDecorator):
    def play_sample(self) -> None:
        print('+ adding distortion')
        super().play_sample()


# client code
def play_instrument(instrument_player: InstrumentPlayer) -> None:
    print('Starting the instrument player:')
    instrument_player.play_sample()
    print()


if __name__ == "__main__":
    guitar = Instrument('guitar')

    basic = BasicInstrumentPlayer(guitar)

    play_instrument(basic)

    echo = EchoDecorator(basic)
    distortion = DistortionDecorator(basic)

    play_instrument(echo)
    play_instrument(distortion)

    distortion_and_echo = DistortionDecorator(echo)

    play_instrument(distortion_and_echo)

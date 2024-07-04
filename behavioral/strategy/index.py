from __future__ import annotations
from abc import abstractmethod, ABC

"""
consider an app for simutaling musical instruments,
with an iterative panel to display the instruments sounds,
notes, samples and features. The app needs different strategies
for different instruments types.
"""


# Context
class Panel:
    def __init__(self, strategy: InstrumentStrategy) -> None:
        self.strategy = strategy

    @property
    def strategy(self) -> InstrumentStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: InstrumentStrategy) -> None:
        self._strategy = strategy

    def play_sample(self) -> None:
        self.strategy.play_sample()


# Strategy
class InstrumentStrategy(ABC):
    @abstractmethod
    def play_sample(self) -> None:
        pass


# Concrete Strategies
class GuitarStrategy(InstrumentStrategy):
    def play_sample(self) -> None:
        print('Turn on guitar')
        print('Choose guitar pick')
        print('Play chords: G - D - Em - C')


# Concrete Strategies
class DrumStrategy(InstrumentStrategy):
    def play_sample(self) -> None:
        print('Adjust chair height')
        print('Choose drum sticks')
        print('Play drum beats: kick - snare - hi-hat')


if __name__ == '__main__':
    panel = Panel(GuitarStrategy())
    print('Playing guitar sample:')
    panel.play_sample()
    print()

    panel.strategy = DrumStrategy()
    print('Playing drum sample:')
    panel.play_sample()

from abc import ABC, abstractmethod
from time import sleep

"""
consider an app for simulating musical instruments.
The app has different instruments and different kinds of simulators.
We want to add more variations, as more instruments and more simulators.
"""


# Implementation
class SamplePlayer(ABC):
    @abstractmethod
    def play_sample(self) -> None:
        pass


# Concrete Implementation A
class GuitarSamplePlayer(SamplePlayer):
    def play_sample(self) -> None:
        print('♬ Playing guitar strings E, A, D, G, B and E')


# Concrete Implementation B
class PianoSamplePlayer(SamplePlayer):
    def play_sample(self) -> None:
        print('♪ Playing piano keys C, D, E, F, G, A, B, C')


# Abstraction
class InstrumentSimulator:
    def __init__(self, sample_player: SamplePlayer) -> None:
        self.sample_player = sample_player

    def simulate(self) -> None:
        print('\nSimulating instrument:')
        self.sample_player.play_sample()


# Extended Abstraction
class DelayedInstrumentSimulator(InstrumentSimulator):
    def simulate(self) -> None:
        print('\nSimulating instrument with 5s delay:')
        print('Please wait...')
        sleep(5)
        print('Delay over! Simulating instrument:')
        self.sample_player.play_sample()


# client
def play_instrument_simulator(simulator: InstrumentSimulator) -> None:
    simulator.simulate()


if __name__ == '__main__':
    guitar_sample = GuitarSamplePlayer()
    piano_sample = PianoSamplePlayer()

    guitar_simulator = InstrumentSimulator(guitar_sample)

    play_instrument_simulator(guitar_simulator)

    piano_simulator = DelayedInstrumentSimulator(piano_sample)
    play_instrument_simulator(piano_simulator)

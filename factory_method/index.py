from abc import ABC, abstractmethod

# Considerer an app that simulates musical instruments.
# New instruments will be added from time to time,
# so the code should be flexible and easy to add new ones.


# Product
class Instrument(ABC):
    @abstractmethod
    def play_sample(self) -> None:
        pass


# ConcreteProduct1
class Guitar(Instrument):
    def play_sample(self) -> None:
        print('♪ playing melody G - C - D - G')


# ConcreteProduct2
class Drums(Instrument):
    def play_sample(self) -> None:
        print('♫ playing Ba Dum Tss')


# Creator
class Simulation(ABC):
    @abstractmethod
    def create_instrument(self) -> Instrument:
        pass

    def play_quick_demo(self) -> None:
        instrument = self.create_instrument()
        instrument.play_sample()
        pass


# ConcreteCreator1
class GuitarSimulation(Simulation):
    def create_instrument(self) -> Guitar:
        return Guitar()


# ConcreteCreator2
class DrumSimulation(Simulation):
    def create_instrument(self) -> Drums:
        return Drums()


def demo_instrument(simulation: Simulation) -> None:
    simulation.play_quick_demo()


if __name__ == "__main__":
    guitar = GuitarSimulation()
    drums = DrumSimulation()

    print('Lets simulate some instruments: ')
    demo_instrument(guitar)
    demo_instrument(drums)

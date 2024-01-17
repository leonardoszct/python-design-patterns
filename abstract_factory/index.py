from abc import ABC, abstractmethod

# The app separates the instruments into groups,
# and groups of instruments have variants.
# New instruments will be added from time to time,
# so the code should be flexible and easy to add new ones.


# Abstract Product A
class Guitar(ABC):
    @abstractmethod
    def play_sample(self) -> None:
        pass


# Abstract Product B
class Piano(ABC):
    @abstractmethod
    def play_sample(self) -> None:
        pass

    @abstractmethod
    def harmonize(self, collaborator: Guitar) -> None:
        pass


# ConcreteProductA1
class AcousticGuitar(Guitar):
    def play_sample(self) -> None:
        print('♪ playing chords G - D - Em - C on guitar')


# ConcreteProductA2
class EletricGuitar(Guitar):
    def play_sample(self) -> None:
        print('♪ playing chords G - D - Em - C on guitar')

    def turn_on(self) -> None:
        print('✶ turning guitar on')


# ConcreteProductB1
class AcousticPiano(Piano):
    def play_sample(self) -> None:
        print('♪ playing chords C - Am - F - G on piano')

    def harmonize(self, collaborator: AcousticGuitar) -> None:
        print('♬ Acoustic harmonies')
        self.play_sample()
        collaborator.play_sample()


# ConcreteProductB2
class EletricPiano(Piano):
    def play_sample(self) -> None:
        print('♪ playing chords C - Am - F - G on piano')

    def turn_on(self) -> None:
        print('✶ turning piano on')

    def harmonize(self, collaborator: AcousticGuitar) -> None:
        print('♬ Acoustic harmonies')
        self.play_sample()
        collaborator.play_sample()


# Abstract Factory
class StringInstruments(ABC):
    @abstractmethod
    def create_guitar(self) -> Guitar:
        pass

    @abstractmethod
    def create_piano(self) -> Piano:
        pass


# Concrete Factory 1
class AcousticStringInstruments(StringInstruments):
    def create_guitar(self) -> AcousticGuitar:
        return AcousticGuitar()

    def create_piano(self) -> AcousticPiano:
        return AcousticPiano()


# Concrete Factory 2
class EletricStringInstruments(StringInstruments):
    def create_guitar(self) -> EletricGuitar:
        guitar = EletricGuitar()
        guitar.turn_on()
        return guitar

    def create_piano(self) -> EletricPiano:
        piano = EletricPiano()
        piano.turn_on()
        return piano


# Client
def demo_string_instruments(
    stringInstrumentsFactory: StringInstruments
) -> None:
    guitar = stringInstrumentsFactory.create_guitar()
    piano = stringInstrumentsFactory.create_piano()

    piano.harmonize(guitar)


if __name__ == "__main__":
    acoustic = AcousticStringInstruments()
    eletric = EletricStringInstruments()

    print('Lets simulate some acoustic instruments: ')
    demo_string_instruments(acoustic)
    print('\nLets simulate some eletric instruments: ')
    demo_string_instruments(eletric)

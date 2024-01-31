"""
onsider an app for simulating musical instruments.
Until this moment, all instruments were the classic ones,
as guitars and pianos, but now you want to support
eletronic synthesizers too. The app needs to support
the synthesizers even though they have a different interface.
"""


# Target
class ClassicInstrument:
    def __init__(self, name) -> None:
        self.name = name

    def play_sample(self) -> None:
        print(f'♪ playing {self.name} sample')


# Adaptee
class Synthesizer:
    def __init__(self, name) -> None:
        self.name = name

    def play_synth_sample(self) -> None:
        print(f'♬ playing {self.name} sample')


# Adapter
class SynthesizerToInstrumentAdapter(ClassicInstrument, Synthesizer):
    def __init__(self, synthesizer):
        self.synthesizer = synthesizer

    @property
    def name(self) -> str:
        return 'adapted ' + self.synthesizer.name

    def play_sample(self) -> None:
        self.synthesizer.play_synth_sample()


# Client
def play_instrument(instrument: ClassicInstrument):
    print(f'\nExecuting {instrument.name}.play_sample()')

    try:
        instrument.play_sample()
    except AttributeError:
        print(f"✖ {instrument.name} doesn't have a play_sample method")


if __name__ == "__main__":
    print(
            "Playing all instruments by using method "
            "instrument.play_sample()"
    )

    guitar = ClassicInstrument('guitar')
    piano = ClassicInstrument('piano')

    play_instrument(guitar)
    play_instrument(piano)

    synthesizer = Synthesizer('synthesizer')

    play_instrument(synthesizer)

    adapter = SynthesizerToInstrumentAdapter(synthesizer)
    play_instrument(adapter)

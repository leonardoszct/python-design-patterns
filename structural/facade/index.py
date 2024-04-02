"""
Consider an app for simulating the sound of musical instruments.
The app will integrate with an external library, but
it does not want to use all its features or decouple
the code with the library logic, so it will use a facade.
"""


# Subsystem A
class SoundsLib():
    def play_sample(self, sample: str) -> None:
        print(f'SoundsLib: ♪ playing {sample}')

    def add_echo(self, sample: str) -> None:
        print('SoundsLib: + adding echo')
        return f'echoed {sample}'


# Subsystem B
class SoundConversionLib():
    def string_to_wav(self, sample: str) -> None:
        print(f'SoundsConversionLib: generated {sample.replace(" ", "_")}.wav')


# Facade
class SoundHandler():
    def __init__(
            self,
            sounds_lib: SoundsLib,
            sound_conversion_lib: SoundConversionLib
            ) -> None:
        self._sounds_lib = sounds_lib
        self._sound_conversion_lib = sound_conversion_lib

    def play_sample(self, sample: str, add_echo: bool = False) -> None:
        print('SoundHandler requests:')
        if add_echo:
            print('Request SoundsLib to add echo')
            sample = self._sounds_lib.add_echo(sample)
            print(f'Echoed sample: {sample}')

        print('Request SoundConversionLib to convert string to wav')
        self._sound_conversion_lib.string_to_wav(sample)

        print('Request SoundsLib to play sample')
        self._sounds_lib.play_sample(sample)


# client code
def play_instrument(sound_handler: SoundHandler, sample: str) -> None:
    print(f'Playing sample {sample} without echo:')
    sound_handler.play_sample(sample)
    print()

    print(f'Playing sample {sample} with echo:')
    sound_handler.play_sample(sample, add_echo=True)
    print()


if __name__ == "__main__":
    sound_lib = SoundsLib()
    sound_conversion_lib = SoundConversionLib()
    sound_handler = SoundHandler(sound_lib, sound_conversion_lib)
    play_instrument(sound_handler, 'guitar')

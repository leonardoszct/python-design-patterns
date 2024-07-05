from __future__ import annotations
from abc import abstractmethod, ABC


"""
consider an app for playing musical instruments samples.
Users can play and remix those samples to create custom beats and melodies.
There's a feature that allows the users to apply effects to the samples,
like reverb, delay and distortion.
"""


# Component
class Sample(ABC):
    @abstractmethod
    def apply_effect(self, effect: Effect) -> None:
        pass


# Concrete Components
class DrumSample(Sample):
    def apply_effect(self, effect: Effect) -> None:
        effect.apply_to_drum(self)

    def play(self) -> None:
        print('♪ Playing drum sample: kick - snare - hi-hat')


# Concrete Components
class GuitarSample(Sample):
    def apply_effect(self, effect: Effect) -> None:
        effect.apply_to_guitar(self)

    def play(self) -> None:
        print('♪ Playing guitar sample: G - D - Em - C')


# Visitor
class Effect(ABC):
    @abstractmethod
    def apply_to_drum(self, sample: DrumSample) -> None:
        pass

    @abstractmethod
    def apply_to_guitar(self, sample: GuitarSample) -> None:
        pass


# Concrete Visitors
class Reverb(Effect):
    def apply_to_drum(self, sample: DrumSample) -> None:
        print('Applying reverb to drum sample')
        sample.play()

    def apply_to_guitar(self, sample: GuitarSample) -> None:
        print('Applying reverb to guitar sample')
        sample.play()


# Concrete Visitors
class Delay(Effect):
    def apply_to_drum(self, sample: DrumSample) -> None:
        print('Applying delay to drum sample')
        sample.play()

    def apply_to_guitar(self, sample: GuitarSample) -> None:
        print('Applying delay to guitar sample')
        sample.play()


# Client
def apply_effect_to_all_samples(samples: list[Sample], effect: Effect) -> None:
    for sample in samples:
        sample.apply_effect(effect)


if __name__ == '__main__':
    samples = [DrumSample(), GuitarSample()]

    print('Applying reverb to all samples:')
    apply_effect_to_all_samples(samples, Reverb())

    print('\nApplying delay to all samples:')
    apply_effect_to_all_samples(samples, Delay())

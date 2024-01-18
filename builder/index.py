from abc import ABC, abstractmethod
from typing import Any

# The app sells guitar and allows the user
# to customize them by choosing different combinations
# of features, like body material and accessories.
# Different guitars should be easy to create.


# Product
class Guitar():
    def __init__(self) -> None:
        self.parts = []

    def add_part(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f'➤ Guitar parts: {", ".join(self.parts)}')


# Builder
class GuitarBuilder(ABC):
    @property
    @abstractmethod
    def guitar(self) -> None:
        pass

    @abstractmethod
    def build_body(self) -> None:
        pass

    @abstractmethod
    def build_neck(self) -> None:
        pass

    @abstractmethod
    def build_head(self) -> None:
        pass

    @abstractmethod
    def build_accessories(self) -> None:
        pass


# Concrete Builder 1
class AcousticGuitarBuilder(GuitarBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._guitar = Guitar()

    @property
    def guitar(self) -> Guitar:
        guitar = self._guitar
        self.reset()
        return guitar

    def build_body(self) -> None:
        return self._guitar.add_part('maple body')

    def build_head(self) -> None:
        return self._guitar.add_part('flat headstock')

    def build_neck(self) -> None:
        return self._guitar.add_part('D-shaped neck')

    def build_accessories(self) -> None:
        return self._guitar.add_part('capo, strap, tuner')


# Director
class CustomGuitars:
    def __init__(self, builder: GuitarBuilder) -> None:
        self._builder = builder

    @property
    def builder(self) -> GuitarBuilder:
        return self._builder

    def build_simple_guitar(self) -> None:
        self.builder.build_body()
        self.builder.build_neck()
        self.builder.build_head()

    def build_guitar_with_accessories(self) -> None:
        self.builder.build_body()
        self.builder.build_neck()
        self.builder.build_head()
        self.builder.build_accessories()


if __name__ == "__main__":
    acousticGuitarBuilder = AcousticGuitarBuilder()
    customGuitars = CustomGuitars(acousticGuitarBuilder)

    print('Generating simple acoustic guitar:')
    customGuitars.build_simple_guitar()
    acousticGuitarBuilder.guitar.list_parts()

    print('\nGenerating acoustic guitar with accessories:')
    customGuitars.build_guitar_with_accessories()
    acousticGuitarBuilder.guitar.list_parts()

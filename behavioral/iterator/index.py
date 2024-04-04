from __future__ import annotations
from collections.abc import Iterable, Iterator

"""
consider an app for listing musical instruments.
The app has a large number of instruments objects
that compose a collection, which needs to be iterated
 in order to perform operations and display
 information about each instrument.
"""


"""
To create an iterator in Python, there are two abstract classes from the built-
in `collections` module - Iterable,Iterator. We need to implement the
`__iter__()` method in the iterated object (collection), and the `__next__ ()`
method in theiterator.
"""


# helper class - not part of the pattern
class Instrument:
    def __init__(self, name: str) -> None:
        self._name = name


# Concrete Interator
class InstrumentIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: Instrument, reverse=False):
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self) -> Instrument:
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


# Concrete Collection
class InstrumentsCollection(Iterable):
    def __init__(self, collection: list[Instrument] | None = None) -> None:
        self._collection = collection or []

    def __getitem__(self, index: int) -> Instrument:
        return self._collection[index]

    def __iter__(self) -> InstrumentIterator:
        return InstrumentIterator(self)

    def get_reserve_iterator(self) -> InstrumentIterator:
        return InstrumentIterator(self, True)

    def add_instrument(self, instrument: Instrument) -> None:
        self._collection.append(instrument)


if __name__ == "__main__":
    collection = InstrumentsCollection()
    collection.add_instrument(Instrument("Guitar"))
    collection.add_instrument(Instrument("Drums"))
    collection.add_instrument(Instrument("Violin"))

    print("Straight traversal:")
    print("\n".join([instrument._name for instrument in collection]))

    print("\nReverse traversal:")
    print("\n".join([
        instrument._name for instrument in collection.get_reserve_iterator()
        ]))

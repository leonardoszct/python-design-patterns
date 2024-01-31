import copy

"""
An app for listing musical instruments specs.
The app has a function to add new instruments
based on a template
"""


# Self Referencing Entity
class InstrumentHistory:
    def __init__(self) -> None:
        self.parent = None

    def set_parent(self, version) -> None:
        self.parent = version


# Some Component
class Guitar:

    """
    Python provides its own interface of Prototype via `copy.copy` and
    `copy.deepcopy` functions. And any class that wants to implement custom
    implementations have to override `__copy__` and `__deepcopy__` member
    functions.
    """

    def __init__(
            self,
            name: str,
            accessories: list[str],
            history: InstrumentHistory,
            ):
        self.name = name
        self.accessories = accessories
        self.history = history

    def __copy__(self):
        accessories = copy.copy(self.accessories)
        history = copy.copy(self.history)

        newGuitar = self.__class__(
            self.name, accessories, history
        )

        newGuitar.__dict__.update(self.__dict__)

        return newGuitar

    def __deepcopy__(self, memo={}):
        """
        The memo argument is used to track objects that have already
        been copied during the deep copy process. It is a dictionary
        that maps original objects to their corresponding copies.
        This is used to handle circular references and prevent the
        copying process from entering an infinite loop.
        """

        accessories = copy.deepcopy(self.accessories, memo)
        history = copy.deepcopy(self.history, memo)

        newGuitar = self.__class__(
            self.name, accessories, history
        )

        newGuitar.__dict__ = copy.deepcopy(self.__dict__, memo)

        return newGuitar

    def print(self, identifier: str):
        print(f'\n♫ {identifier} info:')
        print(f'Name: {self.name}')
        print('Accessories: ')
        for accessory in self.accessories:
            print(f'\t {accessory}')
        print()


def shallow_copy_handler(guitar: Guitar) -> None:
    print('Using shallow copy'.center(80, "-"))
    shallow_copy_guitar = copy.copy(guitar)

    print('Shallow copy of basic guitar generated: ')
    shallow_copy_guitar.print('Shallow')

    print('\nWhen we add  "metronome" to shallow copy guitar accessories...')
    shallow_copy_guitar.accessories.append('metronome')

    if guitar.accessories[-1] == 'metronome':
        print('metronome is also added in basic guitar')
    else:
        print('metronome is not added in basic guitar')

    guitar.print('Basic')

    print("\n"
          "When we change 'capo' accessory to 'case' in the shallow "
          "copy guitar...")

    shallow_copy_guitar.accessories[0] = 'case'

    if "case" in guitar_accessories:
        print('"capo" was also updated to "case" in the basic guitar')
    else:
        print('"capo" was not updated to "case" in the basic guitar')

    guitar.print('Basic')


def deep_copy_handler(guitar: Guitar) -> None:

    print('Using deep copy'.center(80, "-"))
    deep_copy_guitar = copy.deepcopy(guitar)

    print('Deepcopy of basic guitar generated: ')
    deep_copy_guitar.print('Deepcopy')

    print('\nWhen we add  "straps" to deepcopy guitar accessories...')
    deep_copy_guitar.accessories.append('straps')

    if guitar.accessories[-1] == 'straps':
        print('straps is also added in basic guitar')
    else:
        print('straps is not added in basic guitar')

    guitar.print('Basic')

    print("\n"
          "When we change 'case' accessory to 'tuner' in the "
          "deepcopy guitar...")

    deep_copy_guitar.accessories[0] = 'tuner'

    if "tuner" in guitar_accessories:
        print('"case" was also updated to "tuner" in the basic guitar')
    else:
        print('"case" was not updated to "tuner" in the basic guitar')

    guitar.print('Basic')

    history_id = id(deep_copy_guitar.history.parent)
    second_layer_history_id = id(
        deep_copy_guitar.history.parent.history.parent
    )

    if history_id == second_layer_history_id:
        print('Parent (circular ref) has the same id when using '
              'deepcopy copy')
    else:
        print('Parent(circular ref) has not same id when using '
              'deepcopy copy')


if __name__ == "__main__":
    guitar_accessories = [
        "capo",
        {
            "pedal",
            "cable",
        },
        [
            "0.6mm guitar pick",
            "1.5mm guitar pick",
        ]
    ]

    guitar_history = InstrumentHistory()
    guitar = Guitar(
        name="basic",
        accessories=guitar_accessories,
        history=guitar_history
        )
    guitar_history.set_parent(guitar)

    print('Basic guitar generated: ')
    guitar.print('Basic')

    shallow_copy_handler(guitar)
    deep_copy_handler(guitar)

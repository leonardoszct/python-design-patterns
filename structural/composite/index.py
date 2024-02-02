from abc import ABC

"""
onsider an app for selling musical instruments.
The app has two types of objects: Kit and Instrument.
A kit is a collection of smaller kits or several instruments.
A sale could contain a single instrument or a kit of instruments or other kits.
"""


# Component
class CartItem(ABC):
    def __init__(self, price: int, name: str) -> None:
        self._price = price
        self._name = name

    @property
    def parent(self) -> "CartItem":
        return self._parent

    @parent.setter
    def parent(self, parent: "CartItem") -> None:
        self._parent = parent

    def add(self, cart_item: "CartItem") -> None:
        pass

    def remove(self, cart_item: "CartItem") -> None:
        pass

    def is_composite(self) -> bool:
        return False

    def get_price(self) -> str:
        pass

    def print(self, tab_count: int) -> None:
        pass


# Leaf
class Instrument(CartItem):
    def get_price(self) -> int:
        return self._price

    def print(self, tab_count: int = 0) -> None:
        tab = '\t' * tab_count

        print(f'{tab}♩ Instrument "{self._name}" = ${self._price}')


# Composite
class Kit(CartItem):
    def __init__(self, price: int, name: str) -> None:
        super().__init__(price, name)
        self._children = []

    def add(self, cart_item: CartItem) -> None:
        self._children.append(cart_item)
        cart_item.parent = self

    def remove(self, cart_item: CartItem) -> None:
        self._children.remove(cart_item)
        cart_item.parent = None

    def is_composite(self) -> bool:
        return True

    def get_price(self) -> int:
        sum = self._price

        for child in self._children:
            sum += child.get_price()

        return sum

    def print(self, tab_count: int = 0) -> None:
        tab = '\t' * tab_count
        print(f'{tab}♬ Kit "{self._name}" - ${self._price} - Items:')
        for child in self._children:
            child.print(tab_count + 1)


def show_cart_details(cart_item: CartItem) -> None:
    print(f'\nCart details for "{cart_item._name}":')
    cart_item.print(1)
    print(f'\n\tTotal price: ${cart_item.get_price()}')


def add_gift_to_cart(cart_item: CartItem, gift: CartItem) -> None:
    if cart_item.is_composite():
        cart_item.add(gift)
        show_cart_details(cart_item)
    else:
        kit = Kit(0)
        kit.add(cart_item)
        kit.add(gift)
        show_cart_details(kit)


if __name__ == "__main__":
    snare_drum = Instrument(20, "Snare Drum")
    bass_drum = Instrument(20, "Bass Drum")

    hi_tom = Instrument(15, "Hi Tom")
    mid_tom = Instrument(15, "Mid Tom")
    floor_tom = Instrument(15, "Floor Tom")
    tom_kit = Kit(0, 'Tom Kit')
    tom_kit.add(hi_tom)
    tom_kit.add(mid_tom)
    tom_kit.add(floor_tom)

    ride_cymbal = Instrument(10, "Ride Cymbal")
    crash_cymbal = Instrument(10, "Crash Cymbal")
    cymbal_kit = Kit(0, 'Cymbal Kit')
    cymbal_kit.add(ride_cymbal)
    cymbal_kit.add(crash_cymbal)

    drum_kit = Kit(5, 'Drum Kit')
    drum_kit.add(snare_drum)
    drum_kit.add(bass_drum)
    drum_kit.add(tom_kit)
    drum_kit.add(cymbal_kit)

    show_cart_details(snare_drum)
    show_cart_details(bass_drum)
    show_cart_details(tom_kit)
    show_cart_details(cymbal_kit)
    show_cart_details(drum_kit)

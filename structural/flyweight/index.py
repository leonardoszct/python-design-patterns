"""
consider a virtual piano player app. The app shows a
digital piano interface where users can click on each
key to play its related sound.
"""


# Flyweight
from typing import Dict


class Key():
    def __init__(self, name: str, color: str) -> None:
        self.name = name
        self.color = color

    def get_render_info(self, sound: str, status: str) -> None:
        return {
            'name': self.name,
            'color': self.color,
            'sound': sound,
            'pressed': status == 'down'
        }


# FlyweightFactory
class KeyFactory():
    _keys: Dict[str, Key] = {}

    def __init__(self, initial_keys: Dict) -> None:
        for state in initial_keys:
            name, color = state['name'], state['color']
            key_id = self.get_key_id(name, color)
            self._keys[key_id] = Key(name, color)

    def get_key_id(self, name: str, color: str) -> str:
        return '_'.join([name, color])

    def get_key(self, name: str, color: str) -> Key:
        key_id = self.get_key_id(name, color)
        if not self._keys.get(key_id):
            print(f'KeyFactory: can`t find key {key_id}. Creating new one.')
            self._keys[key_id] = Key(name, color)
        else:
            print(f'KeyFactory: key {key_id} already existis, reusing it.')

        return self._keys[key_id]

    def list_keys(self) -> None:
        print(f'{len(self._keys)} Keys in factory:')
        for key in self._keys:
            print(f'Key: {key}')


# client code
def add_key_to_renderer(
        factory: KeyFactory,
        name: str,
        color: str,
        sound: str,
        status: str
        ) -> None:
    print('\nClient: adding key to renderer')
    key = factory.get_key(name, color)
    print(key.get_render_info(sound, status))


if __name__ == "__main__":
    factory = KeyFactory([
        {'name': 'C', 'color': 'white'},
        {'name': 'C#', 'color': 'black'},
        {'name': 'D', 'color': 'white'},
        {'name': 'D#', 'color': 'black'},
        {'name': 'E', 'color': 'white'},
    ])

    factory.list_keys()

    add_key_to_renderer(factory, 'C', 'white', 'do', 'down')
    add_key_to_renderer(factory, 'F', 'white', 'fa', 'up')

    print()
    factory.list_keys()

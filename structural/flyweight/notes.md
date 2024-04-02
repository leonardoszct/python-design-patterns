# Flyweight

> [!IMPORTANT]
> This is my personal notes of [Refactoring Guru's article on Flyweight](https://refactoring.guru/design-patterns/flyweight). Visit their site for a complete version 🤓

### Notes

- **Intent**: provides a way to share common parts of state between different objects so more of that objects can fit into the available amount of RAM.

- **Problem:** consider a virtual piano player app. The app shows a digital piano interface where users can click on each key to play its related sound. Each key is represented as a class `Key`, which has a lot of props, such as name, sound, status and color. As the user plays a song, a lot of `Key` objects are created, leading to a crash because of an insufficient amount of RAM. 

- **Solution:** identify which parts of a `Key` are unique to each object or/and mutable over the execution time, and which are common and/or constant. 
  - unique/mutable: sound and status
    - It's called *extrinsic state* and it can be altered from the outside, by other objects 
  - common/constant: name and color
    - It's called *intrinsic state* and other objects can read it, but not change it
The solution is to stop storing the extrinsic state inside the actual object and only passes it to specific methods which rely on it. The intrinsic state is the only that should be kept withing the onject, being reusable in different contexts. 

  Then, we would create two separated arrays `keys` to store intrinsic state data and `playableKeys` to store the extrinsic state. When creating a new key:
  1. go over `keys` and try to find one with the given name and color. If there's none then create a new one
  2. create a new `playedKeys` with given sound and status and the data from step 1.  
  
  
- **Structure:**
  - **Flyweight**: contains the sharable parts of the original object (e.g `Keys`). It stores the *intrisic* state, and it receives the *extrinsic* state into its methods.
  - **Context**: a class that contains the *extrinsic* state, which is unique accross all original objects (e.g. `PlayableKey`). When combined with a flyweight object, it represents the full state of the original object.
  - **Client**: calculates or stores the extrinsic state oof flyweights.
  - **Flyweight Factory**: manages a pool of existing flyweights. It creates flyweights for the client, storing them to use on future calls. 

- **Applicability**
  - Only when the program must support a huge number of objects which can't fit into the RAM 

### Output

The `decorator/index.py` execution output is:

```cmd
5 Keys in factory:
Key: C_white
Key: C#_black
Key: D_white
Key: D#_black
Key: E_white

Client: adding key to renderer
KeyFactory: key C_white already existis, reusing it.
{'name': 'C', 'color': 'white', 'sound': 'do', 'pressed': True}

Client: adding key to renderer
KeyFactory: can`t find key F_white. Creating new one.
{'name': 'F', 'color': 'white', 'sound': 'fa', 'pressed': False}

6 Keys in factory:
Key: C_white
Key: C#_black
Key: D_white
Key: D#_black
Key: E_white
Key: F_white
```

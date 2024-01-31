# Prototype

> [!IMPORTANT]
> This is my personal notes of [Refactoring Guru's article on Prototype](https://refactoring.guru/design-patterns/prototype). Visit their site for a complete version 🤓

### Notes

- **Intent**: copy existing objects without depending on the objects classes

- **Problem:** consider an app for listing musical instruments specs. The app has a function to add new instruments based on a template. For example, a user wants to add a new guitar based on a guitar that are already listed. To do that, we can create a copy of the existing guitar by creating a new `Guitar` object and copping all props to it. Doing that can be trick if the existing guitar has private properties. Also, to do that that would create an extra dependency on the `Guitar` class.

- **Solution:**
    The pattern declares a common interface to all related objects and adds a clone method in there, so the cloning process is resposability of the object being cloned. 
    - `Instrument` would be the interface implemented by `Guitar`
    - `eletricGuitar = Guitar(type="eletric", color="custom" )`
    - `newEletricGuitar = genericGuitar.clone()`
    This method `clone` would create an object with the same class of the current one and copy all props values to the new one, including private fields.
    So, you can create a set of objects with specific configurations, then you use those to create new objects with the desired config. 
  

- **Structure:**
  - **Prototype**: interfaces with the clone method (e.g. `Instrument`)
  - **Concrete Prototype**: implementations of prototype interface with the clone method, which may also handle edge cases when cloning (e.g. `Guitar` and `Violin`)
  - ***Prototype Registry***: stores the built objects and provides a way to easily access them. 
  

- **Applicability**
  - When copying objects can not rely on the object class.
  - To reduce the number os subclasses that only differ in the initialization of their objects


### Output

The `prototype/index.py` execution output is:

```cmd
Basic guitar generated: 

♫ Basic info:
Name: basic
Accessories: 
         capo
         {'pedal', 'cable'}
         ['0.6mm guitar pick', '1.5mm guitar pick']

-------------------------------Using shallow copy-------------------------------
Shallow copy of basic guitar generated: 

♫ Shallow info:
Name: basic
Accessories: 
         capo
         {'pedal', 'cable'}
         ['0.6mm guitar pick', '1.5mm guitar pick']


When we add  "metronome" to shallow copy guitar accessories...
metronome is also added in basic guitar

♫ Basic info:
Name: basic
Accessories: 
         capo
         {'pedal', 'cable'}
         ['0.6mm guitar pick', '1.5mm guitar pick']
         metronome


When we change 'capo' accessory to 'case' in the shallow copy guitar...
"capo" was also updated to "case" in the basic guitar

♫ Basic info:
Name: basic
Accessories: 
         case
         {'pedal', 'cable'}
         ['0.6mm guitar pick', '1.5mm guitar pick']
         metronome

--------------------------------Using deep copy---------------------------------
Deepcopy of basic guitar generated: 

♫ Deepcopy info:
Name: basic
Accessories: 
         case
         {'pedal', 'cable'}
         ['0.6mm guitar pick', '1.5mm guitar pick']
         metronome


When we add  "straps" to deepcopy guitar accessories...
straps is not added in basic guitar

♫ Basic info:
Name: basic
Accessories: 
         case
         {'pedal', 'cable'}
         ['0.6mm guitar pick', '1.5mm guitar pick']
         metronome


When we change 'case' accessory to 'tuner' in the deepcopy guitar...
"case" was not updated to "tuner" in the basic guitar

♫ Basic info:
Name: basic
Accessories: 
         case
         {'pedal', 'cable'}
         ['0.6mm guitar pick', '1.5mm guitar pick']
         metronome

Parent (circular ref) has the same id when using deepcopy copy
```

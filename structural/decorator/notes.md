# Decorator

> [!IMPORTANT]
> This is my personal notes of [Refactoring Guru's article on Decorator](https://refactoring.guru/design-patterns/decorator). Visit their site for a complete version 🤓

### Notes

> Also known as Wrapper 

- **Intent**: allows to attach new behaviors to existing objects by putting the object inside a specific wrapper object that contain the behaviours.

- **Problem:** consider an app for simulating the sound of musical instruments. The app was created around the `InstrumentPlayer` class, which has a couple fields and a `play` method. At some point, the app needs to add some effects to the instrument's sounds, like distortion and echo. To do that, we could extend `InstrumentPlayer` and put additional methods to into the new subclasses, but that would not allow us to easily combine effects together without having to create more subclasses to each combination. 

- **Solution:** creating a wrapper/decorator that will *contain* another object and the same methods as the target object. The wrapper will delegate all requests to the contained object, but it can alter the result by addind a custom behaviour before or after delegating it.   

- **Structure:**
  - **Component**: common interface for wrappers and wrapped objects (e.g. `InstrumenPlayer`)
  - **Concrete Component**: defines the basic behaviour of the objects being wrapped (e.g. `BasicInstrumentPlayer`) 
  - **Base Decorator**: has a field for referecing a wrapped object, which type will be the component's interface. It delegates all operations to the wrapped object 
  - **Concrete Decorators**: add extra behaviours to the components by overriding methods and executing their specific behaviours after or before calling the parent method.
  - **Client**: can wrapp components in multiple layers of decorators.

- **Applicability**
  - When adding extra behaviours to objexts at runtime
  - When akward or not possible to extend an object's behaviour using inheritance

### Output

The `decorator/index.py` execution output is:

```cmd
Starting the instrument player:
♪ playing guitar

Starting the instrument player:
+ adding echo
♪ playing guitar

Starting the instrument player:
+ adding distortion
♪ playing guitar

Starting the instrument player:
+ adding distortion
+ adding echo
♪ playing guitar
```

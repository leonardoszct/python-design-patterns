# Facade

> [!IMPORTANT]
> This is my personal notes of [Refactoring Guru's article on Facade](https://refactoring.guru/design-patterns/facade). Visit their site for a complete version 🤓

### Notes

- **Intent**: provides a simplidied interface to a external set of assets (such as libraries, frameworks or a set of classes).

- **Problem:** consider an app for simulating the sound of musical instruments. The app uses an external library `SoundsLib` to manipulate sound files. This external library has a lot of features, like adding effects, converting audio file to multiple formats and editing. For the app to use the library, it needs to initialize a lot of objects from it, keep track of its dependencies and call methods in the correct order. If all that is spread around the code base, it will couple the implementation and business logic with the external library, which will make it hard to understand, maintain and to change to a different library later on.  

- **Solution:** creating a class that provides a simple interface to the library. It would only include the relevant features for the app and keep them separated from the rest of the code base. 
  
- **Structure:**
  - **Facade**: class to provide access to particular parts of subsystem's functionality. It knows how to operates the subsystem to handle requests from the client (e.g `SoundHandler`).
  - **Additional Facade**: help prevent polluting a single facade with unrelated features that can have complex structures (e.g. `SoundConversionHandler`) 
  - **Complex Subsystem**: a large set of various objects, which requires complex processes to use their functionalities, like initializing objects in the correc order and supplying them with specific data (e.g. `SoundsLib`). 
  - **Client**: uses facade instead of calling the subsystem directly.

- **Applicability**
  - When needs a symple way to use features from a complex subsystem 
  - When needs to structure a subsystem into layers. 

### Output

The `decorator/index.py` execution output is:

```cmd
Playing sample guitar without echo:
SoundHandler requests:
Request SoundConversionLib to convert string to wav
SoundsConversionLib: generated guitar.wav
Request SoundsLib to play sample
SoundsLib: ♪ playing guitar

Playing sample guitar with echo:
SoundHandler requests:
Request SoundsLib to add echo
SoundsLib: + adding echo
Echoed sample: echoed guitar
Request SoundConversionLib to convert string to wav
SoundsConversionLib: generated echoed_guitar.wav
Request SoundsLib to play sample
SoundsLib: ♪ playing echoed guitar
```

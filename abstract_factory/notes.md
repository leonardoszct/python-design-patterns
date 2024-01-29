# Abstract Factory

> [!IMPORTANT]
> This is my personal notes of [Refactoring Guru's article on Abstract Factory](https://refactoring.guru/design-patterns/abstract-factory). Visit their site for a complete version 🤓

### Notes

- **Intent**: allows to produce families of related objects without having to specity their classes

- **Problem:** consider an app for simulating musical instruments. The app separates the instruments into groups, for example, a group for string instruments would include `Guitar`, `Piano` and `Harp`. String instruments also have some variants, like `Acoustic` and `Eletric`. So, the app code needs to be able to create an  individual instrument in a way that it would match the other instruments in a group.
Also, it should be easy to add new instruments, groups and variants.   

- **Solution:**
    Create interfaces for each instruments, then each variant would have its own interface and implemet that instrument. Examples:
    - `Guitar` would be implemented by `AcousticGuitar` and `EletricGuitar`
    - `Piano` would be implemented by `AcousticPiano` and `EletricPiano`
    - `Harp` would be implemented by `AcousticHarp` and `EletricHarp`
    
    After that, we create an interface for the abstract factory, which would have a create method for each of the instruments in a group. Those methods will return the instrument interface. Examples:
    - `StringInstruments.create_guitar() -> Guitar`
    - `StringInstruments.create_piano() -> Piano`
    - `StringInstruments.create_harp() -> Harp`

    That group interface will be implemented by each of the variants, and in each of them, the methods will return the respective instrument variant. Example:
    - `AcousticStringInstruments.create_guitar() -> AcousticGuitar` 
    - `EletricStringInstruments.create_guitar() -> EletricGuitar` 


- **Structure:**
  - **Abstract Products**: interfaces for the distintic objects in a group (e.g. `Guitar`)
  - **Concrete Products**: implementations of abstract products for all variants (e.g. `AcousticGuitar` and `EletricGuitar`)
  - **AbstractFactory**: interface with creation methods for each products in a group (e.g. `StringInstrumentals`)
  - **Concrete Factories**: implementation of abstract factory for each group variant (e.g `AcousticGuitar` and `EletricGuitar`)
  

- **Applicability**
  - Applications in which objects are related and should be categorized into groups, and the groups have different variations. Then, you want to keep it flexible and easy to add new objects and variants.
  - When a class has a lot of factory methods and that its making it hard to see its promary responsability


### Output

The `abstract_factory/index.py` execution output is:

```cmd
Lets simulate some acoustic instruments: 
♬ Acoustic harmonies
♪ playing chords C - Am - F - G on piano
♪ playing chords G - D - Em - C on guitar

Lets simulate some eletric instruments: 
✶ turning guitar on
✶ turning piano on
♬ Acoustic harmonies
♪ playing chords C - Am - F - G on piano
♪ playing chords G - D - Em - C on guitar
```

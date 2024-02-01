# Bridge

> [!IMPORTANT]
> This is my personal notes of [Refactoring Guru's article on Bridges](https://refactoring.guru/design-patterns/bridge). Visit their site for a complete version 🤓

### Notes

- **Intent**: splits a large class or a set of related classes into two parts (abstraction and implementation) and allow those parts to be developed independently.
  - *Abstraction* (*or interface*) is athe high-lvel control layer of an entity. It is not supposed to execute real work, it should delebate the work to the *implementation* layer (also called *platform*) 

- **Problem:** consider an app for simulating musical instruments. The app has different instruments and different kinds of simulators. We want to add more variations, as more instruments and more simulators, but keeping the hierarchy will make it grow exponentially because the domain is growing in two different dimensions.

- **Solution:** replace inheritance with object composition, which means, turn one of the "dimensions" (color or type) into a separated class hierarchy, and the other dimension will contain the new one as a prop, and object instance. Examples:
  - `GuitarSamplePlayer` will implement `SamplePlayer` as a instrument variation
  - `DelayedInstrumentSimulator` will implement `InstrumentSimulator` as a simulator variation
  - Every `InstrumentSimulator` will have a sample player object as prop

- **Structure:**
  - **Abstraction**: high-level control logic that depends on the implementation to do low-level work (e.g. `InstrumentSimulator`)
  - **Implementation**: declares the interface that's common for all concrete implementations. It declares the methods that allows the abstraction to communicate with the implementation. (e.g. `SamplePlayer`) 
  - **Concrete Implementations**: plataform specific code (e.g. `GuitarSamplePlayer`) 
  - **Redefined Abstractions**: variants of control implepmentations (e.g `DelayedInstrumentSimulator`)


- **Applicability**
  - When dividing and organizing a monolithic class that was multiple variants of same functionality
  - When extend a class in multiple and independent dimensions
  - When needs the ability to switch implementations on runtime


### Output

The `bridge/index.py` execution output is:

```cmd
Simulating instrument:
♬ Playing guitar strings E, A, D, G, B and E

Simulating instrument with 5s delay:
Please wait...
Delay over! Simulating instrument:
♪ Playing piano keys C, D, E, F, G, A, B, C
```

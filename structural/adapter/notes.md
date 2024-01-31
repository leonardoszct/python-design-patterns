# Adapter

> [!IMPORTANT]
> This is my personal notes of [Refactoring Guru's article on Adapter](https://refactoring.guru/design-patterns/adapter). Visit their site for a complete version 🤓

### Notes

> Also known as Wrapper 

- **Intent**: provides a way for objects with different interfaces to collaborate

- **Problem:** consider an app for simulating musical instruments. Until this moment, all instruments were the classic ones, as guitars and pianos, but now you want to support eletronic synthesizers too. The problem is that the eletronic systhesizers have a very different interface then a classic instrument.   

- **Solution:** Create an adapter class that will convert all objects into a common interface and provide a way for the objects to collaborate between them. Example:
  - `SynthesizerToClassicAdapter` will addapt a synthesizer interface to the class `ClassicInstrument`


- **Structure:**
  - **Object Adapter**: the adapter implements the interface of one object and wraps another 
    - **Client**: the class that has the existing logic (e.g. `InstrumentSimulation`)
    - **Client Interface**: the protocol that all classes must follow to collaborate with the client code (e.g. `ClassicInstrument`)
    - **Service**: useful class (usually from 3rd-party or legacy) with incompatible interface (e.g. `Synthesizer`) 
    - **Adapter**: the class with the ability to work with the client and the service by implementing the client interface and wrapping the service object. It's ready to take instructions from the client via the client interface and pass them on to the service object in its specific interface (e.g `SynthesizerToClassicAdapter`)

  - **Class Adapter**: the adapter uses inheritance from both objects at the same time (only available on languages that support multiple inheritance)
    - **Class Adapter**: inherits behaviours from both the client and the service and overrides the relevant methods
  

- **Applicability**
  - When a new class has different inferface from existint ones
  - When reusing multiple ixisting subclasses that lacks a functionality that is not on the superclass


### Output

The `abstract_factory/index.py` execution output is:

```cmd
Playing all instruments by using method instrument.play_sample()

Executing guitar.play_sample()
♪ playing guitar sample

Executing piano.play_sample()
♪ playing piano sample

Executing synthesizer.play_sample()
✖ synthesizer doesn't have a play_sample method

Executing adapted synthesizer.play_sample()
♬ playing synthesizer sample
```

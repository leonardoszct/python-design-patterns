# Factory Method

> [!IMPORTANT]
> This is my personal notes of [Refactoring Guru's article on Factory Method](https://refactoring.guru/design-patterns/factory-method). Visit their site for a complete version 🤓

### Notes

- **Intent**: an interface to create objects in a superclass, but allows subclasses to customize the object being created so it matches a certain context.
  
- **Problem:** consider an app for simulating musical instruments. Until now, the app only simulates guitars and all the codebase is coupled around the `Guitar` class. Now, the app wants to simulate drums as well.
To add a new class `Drums` into the app means making a lot of big changes to the code base, and that process would repeat for any other kind of property the office wants to sell.

- **Solution:** Replace all direct object construcion calls (`new` operator) with calls to a factory method `Simulation.create_instrument` that will create property objects and return them. Each subcass can now override the factory method and change the class of the object being created. Examples:
    - `Simulation.create_instrument() -> Instrument`
    - `GuitarSimulation.create_instrument() -> Guitar`
    - `DrumsSimulation.create_instrument() -> Drums`

- **Structure:**
    - **Product:** declares the interface common to all objects (e.g. `Instrument` )
    - **Concrete Products:** are the different implementations of the product interface (e.g. `Guitar` and `Drums`)
    - **Creator:** is the class that decalres the factory method that will return the new product objects. It has the return type to match the product interface. It can return a default value or be abstract and requires that the subclasses implements their own version (e.g. `Simulation`).
    - **Concrete Creators**: classes that implements the creator and override the factory method (e.g. `GuitarSimulation` and `DrumsSimulation` )

- **Applicability**
    - When you don’t know exactly which types and dependencies the objects of your code and want to keep it flexible
    - When you want to add the ability to extend the default behaviour of a resource, as a library or framework
    - When you want to reuse existing objects instead of recreating them
 

### Output

The `factory_method/index.py` execution output is:

```cmd
Lets simulate some instruments: 
♪ playing chords G - C - D - G
♫ playing Ba Dum Tss

```
# Builder

> [!IMPORTANT]
> This is my personal notes of [Refactoring Guru's article on Builder](https://refactoring.guru/design-patterns/builder). Visit their site for a complete version 🤓

### Notes

- **Intent**: a patterns for constructing different representations of *complex* objects using the same step by step code

- **Problem:** consider an app for selling guitars. Inside the app, there is a feature for the user to customize his instrument by choosing a combination of features, like different body colors/materials, accessories, type of strings, and more. So, the app needs a way to build different types of guitar with all those features combinations.
 
- **Solution:**
    Extract the object construction to a separate object called *Builder* and separate the creation of each feature into a new builder method (step). This way, when creating the object, there is no need to invoke the creation of all features, just the ones that is relevant for that specific variation of it. 
    - `GuitarBuilder.build_strings()`
    - `GuitarBuilder.build_body()`
    - `GuitarBuilder.get_result() -> Guitar`

    Notice that it is possible that a feature has multiple ways to be built, for example, a guitar neck can be C-shaped, D-shape, etc. So, to implement that, we can have different implementations of a builder, which one constructing, step by step, a different variation of the object.
    - `AcousticGuitarBuilder.build_body()`
    - `EletricGuitarBuilder.build_body()`

    **Director**: it's an opitional implementation of a separated class that uses the builder to create the object, but it defines a **specific order** in which the features should be created. It's useful to reuse the objects creation across the code, instead of having the client to direct call the builder and define the order of the steps.


- **Structure:**
  - **Builder**: interface with the common steps to build a product (e.g. `GuitarBuilder`)
  - **Concrete Builder**: implements the builder with different steps implementations (e.g. `AcousticGuitarBuilder` and `EletricGuitarBuilder`)
  - **Products**: objects produced by the builders (e.g. `AcousticGuitar`).
  - **Director **: defines the steps order to build a specific product
  

- **Applicability**
  - When you want to replace the usage of constructors with a lot of optional parameters
  - When you want the ability to create different representations of a product
  - When constructing complex objects (e.g. [composite trees](https://refactoring.guru/design-patterns/composite))
 


### Output

The `builder/index.py` execution output is:

```cmd
Generating simple acoustic guitar:
➤ Guitar parts: maple body, D-shaped neck, flat headstock

Generating acoustic guitar with accessories:
➤ Guitar parts: maple body, D-shaped neck, flat headstock, capo, strap, tuner
```

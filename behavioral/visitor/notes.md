# Visitor

> [!IMPORTANT]
> This is my personal notes of [Refactoring Guru's article on Visitor](https://refactoring.guru/design-patterns/visitor). Visit their site for a complete version 🤓

### Notes

- **Intent**: separates algorithms from the objects they operate. 

- **Problem:** consider an app for playing musical instruments samples. Users can play and remix those samples to create custom beats and melodies. There's a feature that allows the users to apply effects to the samples, like reverb, delay and distortion. Each effect is applyed differently for each instrument, and managing that on the instrument class can bring a lot of complexity and scalability problems. 

- **Solution:** place the behaviour into a separate *visitor* class instead of integrating it to the existing classes. The visitor methods accepts the original object as an input for its methods, which allows those methods to perfom operation on the object based on their type.

- **Structure:**
  - **Visitor**: declares a set of methods that takes concrete elements of an object as argument.
  - **Concrete Visitor**: implements different versions of the same behaviour for different concrete elements classes.
  - **Element**: an interface that declares a method for accepting visitors, which have one parameter with the type of the visitor interface. 
  - **Concrete Element**: implements the acceptance method, with the purpose of redirecting the call tothe proper visitor's method that matches the current element class. 
  - **Client**: usually represents a collection or some complex object.

- **Applicability**
  - When needs to perform an operation on all elements of a complex object structure
  - When needs to clean up the business logic of aux behaviours.
  - When a behaviour makes sense only in some classes of a class hierarchy but not all of them  

### Output

The `visitor/index.py` execution output is:

```cmd
Applying reverb to all samples:
Applying reverb to drum sample
♪ Playing drum sample: kick - snare - hi-hat
Applying reverb to guitar sample
♪ Playing guitar sample: G - D - Em - C

Applying delay to all samples:
Applying delay to drum sample
♪ Playing drum sample: kick - snare - hi-hat
Applying delay to guitar sample
♪ Playing guitar sample: G - D - Em - C
```
****
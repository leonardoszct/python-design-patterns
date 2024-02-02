# Composite

> [!IMPORTANT]
> This is my personal notes of [Refactoring Guru's article on Composite](https://refactoring.guru/design-patterns/composite). Visit their site for a complete version 🤓

### Notes

- **Intent**: allows to compose objects into tree structures and work with these structures as individual objects.
> The pattern is a valid option only if the core model of the domain can be represented as a tree

- **Problem:** consider an app for selling musical instruments. The app has two types of objects: `Kit` and `Instrument`. A kit is a collection of smaller kits or several instruments. A sale could contain a single instrument or a kit of instruments or other kits. To determinate the price of a sale can be a challange because you need to understand if a object is a kit or an instrument, and their prices will be accessible in different appoachs.   

- **Solution:** working with both objects through a common interface that will declare a method for calculating the price. That method will work in different ways depending on the object type:
  - If the object is a leaf (it does not have a list of other objects) it will return it's own price.
  - If the object is not a leaf (it has a list of other objects) it will call the method for each object on the list and sum all their prices with its own
  Example:
    - `SellItem` will be the common interface implemented by `Kit` and `Instrument`
    - `SellItem` will have an abstract method `get_price()`
    - `Instrument.get_price()` will return its price
    - `Kit.get_price()` will iterate the list of items and request for their prices


- **Structure:**
  - **Component**: common interface to describe operations common to all objects (e.g. `SellItem`)
  - **Leaf**: a basic element of the tree that has no sub-elements (e.g. `Instrument`) 
  - **Container**: (*aka composite*) is the element that has sub-elements: leaves or other containers (e.g. `Kit`) 
  - **Client**: works with the elements through the component interface

- **Applicability**
  - When implementing a tree-like object
  - When the client code needs to treat leafs and containers in the same way

### Output

The `composite/index.py` execution output is:

```cmd
Cart details for "Snare Drum":
        ♩ Instrument "Snare Drum" = $20

        Total price: $20

Cart details for "Bass Drum":
        ♩ Instrument "Bass Drum" = $20

        Total price: $20

Cart details for "Tom Kit":
        ♬ Kit "Tom Kit" - $0 - Items:
                ♩ Instrument "Hi Tom" = $15
                ♩ Instrument "Mid Tom" = $15
                ♩ Instrument "Floor Tom" = $15

        Total price: $45

Cart details for "Cymbal Kit":
        ♬ Kit "Cymbal Kit" - $0 - Items:
                ♩ Instrument "Ride Cymbal" = $10
                ♩ Instrument "Crash Cymbal" = $10

        Total price: $20

Cart details for "Drum Kit":
        ♬ Kit "Drum Kit" - $5 - Items:
                ♩ Instrument "Snare Drum" = $20
                ♩ Instrument "Bass Drum" = $20
                ♬ Kit "Tom Kit" - $0 - Items:
                        ♩ Instrument "Hi Tom" = $15
                        ♩ Instrument "Mid Tom" = $15
                        ♩ Instrument "Floor Tom" = $15
                ♬ Kit "Cymbal Kit" - $0 - Items:
                        ♩ Instrument "Ride Cymbal" = $10
                        ♩ Instrument "Crash Cymbal" = $10

        Total price: $110
```

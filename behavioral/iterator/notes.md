# Iterator

> [!IMPORTANT]
> This is my personal notes of [Refactoring Guru's article on Iterator](https://refactoring.guru/design-patterns/iterator). Visit their site for a complete version 🤓

### Notes

- **Intent**: provides a way to *traverse* elements of a collection without needing to know the internal structure or details of the objects of that collection.
  > *Traverse* in this context refers to the process of moving through or iterating over the elements of the collection.    

- **Problem:** consider an app for listing musical instruments. The app has a large number of instruments objects that compose a collection, which needs to be iterated in order to perform operations and display information about each instrument. However, the app has multple implementations of those collections with different internal structures depending on the instrument type and category. Travesing these collections can be a challange if you need to handle each collection differently, leading to code duplication and complexity. 

- **Solution:** extract the traversal behavior of a collection into a separate object called an *iterator*. The iterator will implement the algorithm to transverse the collection, alongside with its details (current position and elements left till the end). This allows that several iterators go through the same collection in paralell and independently. 
  They all implement the same interface, usually with one primary method for fetching elements of a collection. The client, using the interface, can keep running this method to go through a collection of any type and using any traversal algorithm.    


- **Structure:**
  - **Iterator** an interface taht declares the required operations for traversing a collection (fetching next, get current position, restarting, etc).
  - **Concrete Iterators**: implements specific algorithms for traversing a collection. It should track the traversal progress on its own.
  - **Collection**: an interface that declares one or multiple methods for getting iterators compatible with the collection. 
  - **Concrete Collections**: returns new instances of a particular concrete iterator class each time the client requests one.
  - **Client**: works with collections and iterators via their interfaces. 

- **Applicability**
  - When there's a collection with complex data structure internally that needs to be hidden from its clients
  - For reducing duplication of traversal code 
  - When adding the ability to traverse different data structures or when their types are unknown

### Output

The `iterator/index.py` execution output is:

```cmd
Straight traversal:
Guitar
Drums
Violin

Reverse traversal:
Violin
Drums
Guitar
```
****
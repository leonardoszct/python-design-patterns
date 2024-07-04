# Strategy

> [!IMPORTANT]
> This is my personal notes of [Refactoring Guru's article on Strategy](https://refactoring.guru/design-patterns/strategy). Visit their site for a complete version 🤓

### Notes

- **Intent**: defines a family of algorithms and put them into separate classes, allowing their objects to interchange between classes. 

- **Problem:** consider an app for simutaling musical instruments, with an iterative panel to display the instruments sounds, notes, samples and features. Naturally, there are different approachs to mount the panel, since there's big differences between some type of instruments, for example, drums, pianos and flutes requires different assets, configurations, apis, etc. Handling those different approaches whithout spliting them, like on a single big file, can bring a lot of troubles as the variety of instruments increase, as maintence difficulty, conflicts, low scalability, and a lot more. 
 
- **Solution:** separate the "different ways" of doing the same thing into different *strategies* classes. The original class, called context, stores a reference (created by the client) to one of the strategies and delegates the work to that strategy. 


- **Structure:**
  - **Context**: stores a reference to one of the strategies and communicate through the strategy interface.
  - **Strategy**: an interface that declares a method for the context to execute a strategy
  - **Concrete Strategies**: implementation different variations of an algorithm
  - **Client**: creates a specific strategy object and passes it to the context

- **Applicability**
  - When using different variants of an algorithm within an object, with ability to switch between strategies
  - When there's a lot of similar classes that only differ in the way they execute a specific behaviour
  - When required to isolate business logic from the implementation details of algorithms taht may not be as important as the context logic
  - When there's a conditional statement to switch between different implementations of the same algorithm

### Output

The `strategy/index.py` execution output is:

```cmd
Playing guitar sample:
Turn on guitar
Choose guitar pick
Play chords: G - D - Em - C

Playing drum sample:
Adjust chair height
Choose drum sticks
Play drum beats: kick - snare - hi-hat
```
****
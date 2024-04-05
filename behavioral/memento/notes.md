# Memento

> [!IMPORTANT]
> This is my personal notes of [Refactoring Guru's article on Memento](https://refactoring.guru/design-patterns/memento). Visit their site for a complete version 🤓

### Notes

- **Intent**: provides a way to save and restore the previous state of an object without revealing the details of its implementation

- **Problem:** consider an app for music composition. The app allows user to add instrument melodies, lyrics and effects to a audio track. It needs to support undo/redo functionality to allow users to revert changes, and to do that it needs to manage the state of a track and restore it to its previous states. However, that can be hard when considering some objects has private assets and a lot of elements are involved.
   
- **Solution:** an object (*originator*) produces a *memento*, which will store the copy of the object state. The memento  content is not accessible to other objects other than it's producer. Other objects must communicate with mementos using a limited interface that allows fetching the snapshot metadata, but not the original object state. 
  Mementos can be stored inside other objects, the *caretakers*, which will not have access to the original object content, but will be able to keep a list of mementos and grab items from that list. 


- **Structure:**
  - **Originator** produce snapshots of its own state, as well as restore its state from a sanpshot 
  - **Memento**: is a value object that acts like the snapshot of the originator's state.  
  - **Caretaker**: knows when and why to capture the originator's state, and when to restore a state.

- **Applicability**
  - When is needed to restore a previous state of an object from a snpashot of the object
  - When direct access to the objectś fields/getters/setters violates its encapsulation.

### Output

The `memento/index.py` execution output is:

```cmd
Creating lyrics...
Lyrics: current state is Lorem ipsum dolor sit amet

LyricsHistory: saving lyrics state
Lyrics: saving current state to memento
Lyrics: setting lyrics
Lyrics: new state is  Consectetur adipiscing elit

LyricsHistory: saving lyrics state
Lyrics: saving current state to memento
Lyrics: setting lyrics
Lyrics: new state is  Sed do eiusmod tempor incididunt ut labore

LyricsHistory: saving lyrics state
Lyrics: saving current state to memento
Lyrics: setting lyrics
Lyrics: new state is  Et dolore magna aliqua

LyricsHistory: list of lytics mementos:
2024-04-04 17:05:50 / (Lorem ips...)
2024-04-04 17:05:50 / ( Consecte...)
2024-04-04 17:05:50 / ( Sed do e...)

Undoing...
LyricsHistory: restoring state to 2024-04-04 17:05:50 / ( Sed do e...)
Lyrics: restoring state to  Sed do eiusmod tempor incididunt ut labore

Undoing...
LyricsHistory: restoring state to 2024-04-04 17:05:50 / ( Consecte...)
Lyrics: restoring state to  Consectetur adipiscing elit
```
****
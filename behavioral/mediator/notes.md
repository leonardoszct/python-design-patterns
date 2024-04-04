# Mediaator

> [!IMPORTANT]
> This is my personal notes of [Refactoring Guru's article on Mediator](https://refactoring.guru/design-patterns/mediator). Visit their site for a complete version 🤓

### Notes

- **Intent**: provides a way to reduce chaotic dependencies between objects by restricting direct communication between objects and forcing them to communicate via a single mediator object.

- **Problem:** consider an app for music composition. The app has a lot of different components like a list of tracks and a sound editing tool. All these components has a visual representation and they need to iteract with each other in a corrdinated way. For example, the editing tool should stay disabled until a track is selected on the list of track. However, we can't directly couple those components because it would make it hard to add new components and still reuse those elements, creating new interactions.  

- **Solution:** remove all direct communication between the components that should be independent of each other. Then, provides a mediator object that will receive a request from a component to another, and redirect that request.    


- **Structure:**
  - **Components** multiple classes with business logic. Each one has a reference to the mediator, declared with the mediator interface type. 
  - **Mediator**: an interface that declares the methods of communication with components, which usually include just a single notification method.  
  - **Concrete Mediators**: encapsulate relationsbetween components.

- **Applicability**
  - When it gets hard to change some of the classes because its coupled to another group of classes
  - When a component can't be reused in a different program becaus it's dependent on other components
  - When it's required to create a lot of components subclasses just to reuse some of its behavior 

### Output

The `decorator/index.py` execution output is:

```cmd
Client: trigger select_track
TrackList: track selected
AdioMediator: event track_selected received
AdioMediator: trigger open_track
AudioEditor: open track on editor
AdioMediator: event open_track received

Client: trigger add_effects
AudioEditor: adding effects
AdioMediator: event add_effects received

Client: trigger save_as_copy
AudioEditor: save track as copy
AdioMediator: event save_as_copy received
AdioMediator: trigger save_track
TrackList: save track
AdioMediator: event save_track received
```
****
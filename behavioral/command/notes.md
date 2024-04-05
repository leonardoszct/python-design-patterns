# Command

> [!IMPORTANT]
> This is my personal notes of [Refactoring Guru's article on Command](https://refactoring.guru/design-patterns/command). Visit their site for a complete version 🤓

### Notes

- **Intent**: turns a request into a stand-alone object, which contains all information about the request, allowing it to be used as a method arggument, deplay or queues and adds support to undoable operations.

- **Problem:** consider an app for music composition. The app has a sound control board with buttons like play, pause, record and stop. All those inherit from a common `Button` class, even though each one is meant to execute a different action upon the click event. 
  One approach is creating one subclass to each of the buttons and handle the click inside the said subclass, but that would result in
  1. an excessive number subclasses 
  2. couple the GUI with thee music logic
  3. redundant code spread around the subclasses for actions that is used on multiple contexts

- **Solution:** extract the request details (like object being called, name of the method and arguments) into a separate *command* class with a single method to trigger the request. It would serve as a link between multiple buttons and the music logic, meaning that the GUI doesn't need to care about the logic, only triggering the command which will process it. 
  All commands needs to implement the same interface, so a single request-sender can use multiple commands without coupling to the concrete classes of commands.    


- **Structure:**
  - **Sender** (aka *involker*): handles the initialization of requests. It has a field for pointing to a command object and triggering it.
  - **Command**: an interface that declares a single method to execute the command.
  - **Concrete Commands**: implements various kinds of requests, but it does not perform the work, but rather pass redirect the call to the business logic object. 
  - **Receiver**: contains business logic and receive the requests triggered by the command, doind the actual work to process them.
  - **Client**: configures concrete command objects. 

- **Applicability**
  - When needs to parametrize objects with operations 
  - When is wanted to queue, schedule or execute operations remotely
  - When is wanted to implement reversible operations

### Output

The `command/index.py` execution output is:

```cmd
AudioBoard: start recording audio
RecordAudioCommand: sending request to IO Controller
AudioIODeviceController: turning on microphone
AudioIODeviceController: recording my_project
AudioIODeviceController: saving my_project
AudioBoard: finished recording audio
PrintAudioInfoCommand: my_project
```
****
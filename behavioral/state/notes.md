# State

> [!IMPORTANT]
> This is my personal notes of [Refactoring Guru's article on State](https://refactoring.guru/design-patterns/state). Visit their site for a complete version 🤓

### Notes

- **Intent**: allows an object to change its behaviour when there are internal changes, as if the object had changed its class.

- **Problem:** consider an app for music composition. The app has a `Project` class which can be in one of three states: `DRAFT`, `COMPLETED` and `PUBLISHED`. There are different rules and behaviours around `publish` or `unpublish` methods: 
  - A `PUBLISHED` project can't be moved to `DRAFT`
  - A `DRAFT` projects can't be moved to `PUBLISHED`
  - A `COMPLETED` object can be moved to `DRAFT` or `PUBLISHED`

This behaviours can be implemented by a *state machine based* algorithm, with a lot of conditional statements. But, that approach requires a certain level of prediction around all possible states and the transition between them. And, as the app evolves, more states and rules can be added, turning the state machine complex and hard to maintain. 


- **Solution:** create new classes for all possible states and let these classes handle all state-specific behaviours internally. The original object (`context`) will not implement all possible behaviours, instead it will stores a reference of the current state and delegates state-related work to that object. Then, to transition one state to another, the `context` will update the reference with the new state. 
  > Different than the Strategy pattern, the states may be aware of each other and initiate transitions from one state to another.    


- **Structure:**
  - **Context**: stores a reference to one of the concrete state objects and delegates state-specific work to it.
  - **State**: an interface that declares state-specific methods
  - **Concrete States**: implementation for the state-specific methods. They may store backreference to the context object. 

- **Applicability**
  - When an object behaves differently depending on it's current state, the number of states is big and there's constant changes to the state-specific code
  - When a class has massive conditionals that alters its behaviours accordingly to class attributes current values
  - When there's a lot of duplicated code accorss similar states and transitions of a condition-based state machine 

### Output

The `state/index.py` execution output is:

```cmd
Project: Initial state is Draft
Execute: Publish project
Draft: can not publish project in DRAFT state. Please save the project first.

Execute: Save project
Draft: saving project.
Project: Transition from Draft to Completed

Execute: Publish project
Completed: publishing project.
Project: Transition from Completed to Published

Execute: Edit project
Published: enabeling edit mode.
Project: Transition from Published to Draft
```
****
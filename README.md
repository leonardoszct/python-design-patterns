# python-design-patterns


## Overview

This project serves as a personal exploration of design patterns in Python. The goal is to deepen understanding and proficiency in Python by implementing various design patterns through practical and simple examples.

My main source of knowladge was the [Refactoring Guru - Design Patterns](https://refactoring.guru/design-patterns) content.

## Project Structure

The project is organized into folders, each representing a specific design pattern. Inside each folder, you will find two key files:

- `notes.md`: personal notes and interpretations of the content from the [Refactoring Guru](https://refactoring.guru/design-patterns) website.

- `index.py`: python script with a simple implementation of the respective design pattern.

## Usage

Run the Python scripts (`index.py`) to see the design patterns in action and experiment with them. 

```cmd
python ${pattern_type}/${pattern_folder_name}/index.py
```

For example, to run the `Factory Method` script, try:

```cmd
python creational/factory_method/index.py

```

## Design Patterns

### Behavioral Patterns
- [Chain of Responsability]('./behavioral/chain_of_responsability')
- [Command]('./behavioral/command')
- [Iterator]('./behavioral/iterator')
- [Mediator]('./behavioral/mediator')
- [Memento]('./behavioral/memento')
- [Observer]('./behavioral/observer')
- [State]('./behavioral/state')
- [Strategy]('./behavioral/strategy')
- [Template Method]('./behavioral/template-method')
- [Visitor]('./behavioral/visitor')

### Creational Patterns

- [Abstract Factory](./creational/abstract_factory/)
- [Builder](./creational/builder/)
- [Factory Method](./creational/factory_method/)
- [Prototype](./creational/prototype/)
- [Singleton](./creational/singleton/)

### Structural Patterns

- [Adapter](./structural/adapter/)
- [Bridge](./structural/bridge/)
- [Composite](./structural/composite/)
- [Decorator](./structural/decorator/)
- [Facade](./structural/facade/)
- [Flyweight](./structural/flyweight/)
- [Proxy](./structural/proxy/)

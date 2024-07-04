from __future__ import annotations
from abc import abstractmethod, ABC

"""
consider an app for music composition.
The app projects can be in one of three states:
DRAFT, COMPLETED and PUBLISHED.
The app needs to handle the transitions between these states and
perform different actions based on the current state of the project.
"""


# Context
class Project:
    _state = None

    def __init__(self, state: ProjectState) -> None:
        self.transition_to(state)

    def transition_to(self, state: ProjectState) -> None:
        new_name = type(state).__name__

        if not self._state:
            print(f'Project: Initial state is {new_name}')
        else:
            current_name = type(self._state).__name__
            print(f'Project: Transition from {current_name} to {new_name}')

        self._state = state
        self._state.project = self

    def handle_publish(self) -> None:
        print('Execute: Publish project')
        self._state.handle_publish()
        print()

    def handle_save(self) -> None:
        print('Execute: Save project')
        self._state.handle_save()
        print()

    def handle_edit(self) -> None:
        print('Execute: Edit project')
        self._state.handle_edit()
        print()


# State
class ProjectState(ABC):
    @property
    def project(self) -> Project:
        return self._project

    @project.setter
    def project(self, project: Project) -> None:
        self._project = project

    @abstractmethod
    def handle_publish(self) -> None:
        pass

    @abstractmethod
    def handle_save(self) -> None:
        pass

    @abstractmethod
    def handle_edit(self) -> None:
        pass


# Concrete State
class Draft(ProjectState):
    def handle_publish(self) -> None:
        print(
            'Draft: can not publish project in DRAFT state. '
            'Please save the project first.'
        )

    def handle_save(self) -> None:
        print('Draft: saving project.')
        self.project.transition_to(Completed())

    def handle_edit(self) -> None:
        print('Draft: project is already editable. No action needed.')


# Concrete State
class Completed(ProjectState):
    def handle_publish(self) -> None:
        print('Completed: publishing project.')
        self.project.transition_to(Published())

    def handle_save(self) -> None:
        print('Completed: project is already saved. No action needed.')

    def handle_edit(self) -> None:
        print('Completed: enabeling edit mode.')
        self.project.transition_to(Draft())


# Concrete State
class Published(ProjectState):
    def handle_publish(self) -> None:
        print('Published: project is already published. No action needed.')

    def handle_save(self) -> None:
        print('Published: can not save project in PUBLISHED state.'
              'Please edit the project first.')

    def handle_edit(self) -> None:
        print('Published: enabeling edit mode.')
        self.project.transition_to(Draft())


if __name__ == '__main__':
    project = Project(Draft())

    project.handle_publish()
    project.handle_save()
    project.handle_publish()
    project.handle_edit()

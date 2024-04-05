from __future__ import annotations
from abc import abstractmethod, ABC
from typing import List

"""
consider an app for selling musical instruments.
Each day, the app randomly chooses one instrument to
sell at a 50% discount. The app needs a feature that
tells them when their desired instrument is on sale.
"""


# Observer
class User(ABC):
    @abstractmethod
    def update(self, subject: NotificationManager) -> None:
        pass


# Concrete Observer
class DesktopUser(User):
    def update(self, instrument: InstrumentOnSaleNotification) -> None:
        if instrument._on_sale:
            print('DesktopUser: sending email for user!')


# Concrete Observer
class MobileUser(User):
    def update(self, instrument: InstrumentOnSaleNotification) -> None:
        if instrument._on_sale:
            print('MobileUser: sending push notification for user!')


# Subject
class NotificationManager(ABC):
    @abstractmethod
    def attach(self, observer: NotificationManager) -> None:
        pass

    @abstractmethod
    def detach(self, observer: NotificationManager) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


# Concrete Subject
class InstrumentOnSaleNotification(NotificationManager):
    _on_sale: bool = False
    _users: List[User] = []

    def attach(self, user: User) -> None:
        print('InstrumentOnSaleNotification: added an user.')
        self._users.append(user)

    def detach(self, user: User) -> None:
        print('InstrumentOnSaleNotification: removed an user.')
        self._users.remove(user)

    def notify(self) -> None:
        print('InstrumentOnSaleNotification: updating all users...')
        for user in self._users:
            user.update(self)

    def add_to_sale(self) -> None:
        print('InstrumentOnSaleNotification: instrument is now on sale.')
        self._on_sale = True
        self.notify()


if __name__ == '__main__':
    desktop_user = DesktopUser()
    mobile_user = MobileUser()

    instrument_on_sale = InstrumentOnSaleNotification()
    instrument_on_sale.attach(desktop_user)
    instrument_on_sale.attach(mobile_user)

    instrument_on_sale.add_to_sale()

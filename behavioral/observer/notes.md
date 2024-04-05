# Observer

> [!IMPORTANT]
> This is my personal notes of [Refactoring Guru's article on Observer](https://refactoring.guru/design-patterns/observer). Visit their site for a complete version 🤓

### Notes

- **Intent**: allows to define a subscription mechanism to notigy multiple objects about any events that happen to the object they're observing

- **Problem:** consider an app for selling musical instruments. Each day, the app randomly chooses one instrument to sell at a 50% discount. For users hoping for a specific instrument to be on sale, they need to check the app daily. However, with many instruments available, they often check in vain. To help these users, the app needs a feature that tells them when their desired instrument is on sale. But sending an email to all users each time an instrument goes on sale would annoy many people, especially those not interested in that instrument.


- **Solution:** create a publisher class that will puslish an event everytime an instrument is on sale. Then, users that are interested in an instrument can subscribe to that event and get notified when it is published. 


- **Structure:**
  - **Publisher**: issues events of interest to other objects. They have a subscription infrastructure that allows news subscribers to join and leave the list.
  > When an event happens, the publisher gover over the subscription list and calls the notification method on each subscriber. 
  - **Subscriber**: interface that declares the notification interface
  - **Concrete Subscribers**: implements the subscriber interface and performs actions in response to notifications issued by the bpublisher 
  - **Client**: creates publisher and subscriber objects, then registers subscribers for publisher updates. 

- **Applicability**
  - When changes to the state of one object may require changes in other objects (which are unknown beforechand)
  - When objects must observe others for a limited time or specific cases.

### Output

The `observer/index.py` execution output is:

```cmd
InstrumentOnSaleNotification: added an user.
InstrumentOnSaleNotification: added an user.
InstrumentOnSaleNotification: instrument is now on sale.
InstrumentOnSaleNotification: updating all users...
DesktopUser: sending email for user!
MobileUser: sending push notification for user!
```
****
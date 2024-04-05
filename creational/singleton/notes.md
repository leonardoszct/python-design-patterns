# Singleton

> [!IMPORTANT]
> This is my personal notes of [Refactoring Guru's article on Singleton](https://refactoring.guru/design-patterns/singleton). Visit their site for a complete version 🤓

### Notes

- **Intent**: a way to ensure that a class has only one instance and that the said instance is available globally

- **Problem:** 
  - 1. Make sure that a class has just a single instance:
    Consider an app that plays instrumental samples on your device. The app has a `SoundPlayer` class that plays the samples on your device speakers. 
    If you have multiple instances of that class, you could have a scenario where a sample is playing and another one starts playing too. 
    So, in this app is important to have only one object integrated with the device speakers, that will make sure only one sample is played at a time.
  - 2. Provide global access point to that instance:
    Considering the same app from problem 1, let's supose there is a lot of places that shows if a sample is current playing, for example, a status bar, a menu, a landing page, etc. It's important that all those objects have access to the exact same information, so we don't end up with different status to the same thing. 

- **Solution:**
    Create a class with a private constructor that prevents other objects to create a new instance. That class will have a static creation method that creates an object and saves that instance to a static property. The static creation method will:
    - check if there is a instance saved on the static property
      - if yes: return that instance
      - if no:
        - create a new instance
        - save new instance to the static property
        - return the instance


- **Structure:**
  - **Singleton**: class with the static method `get_instance` that return an object of the same class od its own (e.g. `SoundPlayer.get_instance() -> SoundPlayer`)


- **Applicability**
  - When a class should not have more than one instance and if the instance should be available globally
  - When need stricter control over global variables



### Output

The `singleton/index.py` execution output is:

```cmd
Created SoundPlayer instance for HOME page

Created SoundPlayer instance for LIKED page

Created SoundPlayer instance for HISTORY page

All instances have the same id, they are the same

Playing samples on HOME page instance:
♪ playing guitar sample - duration: 2s
♪ playing drums sample - duration: 2s

Playing samples on LIKED page instance:
♪ playing piano sample - duration: 3s

When accessing the player HISTORY page:

♫ Player history:
♪ guitar
♪ drums
♪ piano
```

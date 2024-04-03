# Chain of Resposibility

> [!IMPORTANT]
> This is my personal notes of [Refactoring Guru's article on Chain of Responsability](https://refactoring.guru/design-patterns/chain-of-responsability). Visit their site for a complete version 🤓

### Notes

- **Intent**: allows to pass requests along a chain of handlers, and each handler decides to process the request or to pass it to the next object in the chain.

- **Problem:** consider an app to simulate musical instruments. It has a big list of instruments and each instruments has dozen of audio sample files, which are stored on a database. When playing a sample, there's some checks the app needs to make: 
  1. There are free samples and samples only available for premium users, so before playing a sample it needs to check the user's permissions. 
  2. Since the sample files can be big, getting them from the DB uses a lot of resources, so the app keeps a chache for them. Before fetching a sample, it needs to check if it is cached.
  3. Some samples has copy rights and other don't. Before playing them, you have to check so you can allow/block the download option.


- **Solution:** extract each check into its own class (a *handler*) with single method that receives the request and its data, and then perform the check. All handlers will be part of a chain, and each will have a field for pointing to the next handler in the chain. After processing the request internally, the handler will decide if it should pass it to the next handler of stop the propagation of the request. All handler should implement the same interface and each one only cares about the next in line. 
  > There's another approach where only one handler can process the request, and only one handler will process it (or none will).   


- **Structure:**
  - **Handler**: decalres the interface common for all concrete handlers.
  - **Base Handler**: optional classe to put the boilerplate code that's common to all handlers.
  - **Concrete Handlers**: containg the code to execute the requests. It decides if it should process the request and/or pass it to the next one. 
  - **Client**: compose the chain once or dynamically. 

- **Applicability**
  - When the program is expected to process different kinds of requests in various ways, but those requests types and sequences are not known beforehand
  - When is required to execute several handlers in a specific order
  - When a set of handlers and their execution order can change at runtime

### Output

The `decorator/index.py` execution output is:

```cmd
Requesting to play sample sample1
AccessHandler: Access granted to sample sample1
FetchHandler: Sample sample1 fetched from cache
ExportHandler: Sample sample1 cannot be exported
♪ Playing sample sample1

Requesting to play sample sample2
AccessHandler: Access granted to sample sample2
FetchHandler: Sample sample2 fetched from database
ExportHandler: Sample sample2 can be exported
ExportHandler: Sample sample2 cannot be exported
♪ Playing sample sample2

Requesting to play sample sample3
AccessHandler: Access denied to sample sample3
✖ Cannot play sample sample3

Requesting to play sample sample4
AccessHandler: Access granted to sample sample4
FetchHandler: Sample sample4 fetched from database
ExportHandler: Sample sample4 can be exported
ExportHandler: Sample sample4 cannot be exported
♪ Playing sample sample4
```
****
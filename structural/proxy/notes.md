# Proxy

> [!IMPORTANT]
> This is my personal notes of [Refactoring Guru's article on Proxy](https://refactoring.guru/design-patterns/proxy). Visit their site for a complete version 🤓

### Notes

- **Intent**: provides substitute or placeholder for another object, while controling the access to the original object and allowing additional steps before or after the request gets through to the original object. 

- **Problem:** consider an app to simulate musical instruments. It has a big list of instruments and each instruments has dozen of audio sample files, which are stored on a database. Accessing that databse is not always required, only from time to time, and those requests are slow and consumes a vast amount of system resources.  

- **Solution:**  create a new class with the same interface as the service to get those audio samples. Then, the client would use that proxy instead of calling the original service, then you can add extra steps in the proxy before actually requesting the file, such as saving a cache or playing a preview.


- **Structure:**
  - **Service Interface**: decalres the interface of the service, which is implemented by the proxy.
  - **Service**: the class that provides some useful business logic.
  - **Proxy**: implements the service interface and has a reference to the service object. After it finishes its processing, it passes the requests to the service object.
  - **Client**: works with services and proxies via the same interface. 

- **Applicability**
  - Lazy initialization (virtual proxy): when there's a heacyweight sercie object that wastes sustem resorces if it's always up and there's no need for it to be available all the time
  - Access control (protection proxy): restricting the acess to the service to only specific clients
  - Local execution of a remote service (remote proxy): service object is located on a remote service
  - Logging requests (logging proxy): keep a history of requests to the service objext
  - Caching request results (caching proxy): cache resuslts of the client requests and handles the life cycle of this cache
  - Smart reference: keep track of clients and dismiss teh service if no client is requesting the service 

### Output

The `decorator/index.py` execution output is:

```cmd
Client: requesting sample play
SampleProxy: checking access
SampleProxy log:
        error - access denied - guitar - sample1

Client: requesting sample play
SampleProxy: checking access
SampleDBService: fetching sample2 for guitar
SampleProxy log:
        info - get sample - guitar - sample2
```
****
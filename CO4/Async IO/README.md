**Design a High-Throughput Controller Using Asynchronous I/O**

A high-throughput controller is a system that can handle a large number of requests or operations efficiently. Asynchronous I/O allows the program to start an I/O operation and continue doing other work instead of waiting for the operation to finish.

For example, a controller may receive requests from many users and communicate with databases or external APIs.

**Simple Architecture**
             Clients

             
          /     |      \

          
         ↓      ↓       ↓

         
    ┌────────────────────────┐
    
    │  Asynchronous Controller│

    └────────────────────────┘

    
             |
             
       Event Loop
       
             |
             
    ┌────────┼─────────┐
    
    ↓        ↓         ↓
    
 Database   API      File/Network
 
    I/O       I/O        I/O
    
    |         |          |
    
    └─────────┼──────────┘
    
              ↓
              
           Response
           
**## Simple Python Code for a High-Throughput Controller Using Asynchronous I/O**


import asyncio

async def handle_request(request):
    print("Processing", request)

    # Simulate I/O operation
    await asyncio.sleep(2)

    print("Completed", request)


async def main():
    tasks = [
        handle_request("Request 1"),
        handle_request("Request 2"),
        handle_request("Request 3")
    ]

    await asyncio.gather(*tasks)


asyncio.run(main())
```

### Simple Explanation

* `import asyncio` → imports the asynchronous programming module.
* `async def` → creates an asynchronous function.
* `await asyncio.sleep(2)` → simulates an I/O operation, such as a database or network request.
* `tasks` → contains multiple requests.
* `asyncio.gather()` → runs all requests concurrently.
* `asyncio.run(main())` → starts the asynchronous program.

**Output**

Processing Request 1
Processing Request 2
Processing Request 3

Completed Request 1
Completed Request 2
Completed Request 3
```

**### How it works**

```text
Request 1 ──→ Waiting for I/O ──→ Complete
Request 2 ──→ Waiting for I/O ──→ Complete
Request 3 ──→ Waiting for I/O ──→ Complete
```

Instead of waiting for **Request 1** to finish before starting **Request 2**, the program can work on other requests while waiting for I/O.

**Key idea:** `async` + `await` + `asyncio.gather()` allow multiple I/O-bound operations to make progress concurrently.

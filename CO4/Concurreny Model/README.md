**# How to Choose a Concurrency Model**

A **concurrency model** is a way of designing a program so that multiple tasks can make progress at the same time.

The right model depends mainly on **what type of work your program performs**.

**## 1. Main Concurrency Models**

| Model               | Best suited for      | Simple example                 |

| ------------------- | -------------------- | ------------------------------ |

| **Threading**       | I/O-bound tasks      | File/network operations        |

| **Asyncio**         | Many I/O-bound tasks | Web requests, APIs             |

| **Multiprocessing** | CPU-bound tasks      | Calculations, image processing |

| **Sequential**      | Small/simple tasks   | Simple calculations            |

**### Easy rule to remember**

Is the program waiting for I/O?


        |
       YES
       
        ↓
 
 Threading / Asyncio


Is the program doing heavy CPU calculations?

        |
       
       YES
       
        ↓
 
 Multiprocessing


Only a small/simple task?

        |
        
        ↓
 
 Sequential execution

**# 2. Threading — For I/O-Bound Work**

Threads are useful when the program spends a lot of time **waiting**, such as waiting for files, network responses, or database operations.

### Simple code

```python
import threading
import time

def task(name):
    print(name, "started")
    time.sleep(2)
    print(name, "finished")

t1 = threading.Thread(target=task, args=("Task 1",))
t2 = threading.Thread(target=task, args=("Task 2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("All tasks completed")
```

### Output

```text
Task 1 started
Task 2 started
Task 1 finished
Task 2 finished
All tasks completed
```

The exact order may vary.

### Why choose threading?

Both tasks spend most of their time waiting during:

```python
time.sleep(2)
```

So another thread can make progress while one thread is waiting.

---

**# 3. Asyncio — For Many I/O Tasks**

`asyncio` is useful when you have **many I/O operations** that can be handled asynchronously.

### Simple code

```python
import asyncio

async def task(name):
    print(name, "started")
    await asyncio.sleep(2)
    print(name, "finished")

async def main():
    await asyncio.gather(
        task("Task 1"),
        task("Task 2"),
        task("Task 3")
    )

asyncio.run(main())
```

### Output

```text
Task 1 started
Task 2 started
Task 3 started
Task 1 finished
Task 2 finished
Task 3 finished
```

Again, the exact order can vary.

### Why choose asyncio?

Instead of blocking while waiting for I/O, `await` allows the event loop to work on other tasks.

This is especially useful for:

* Web servers
* API requests
* Network applications
* Chat applications
* Database communication

---

**# 4. Multiprocessing — For CPU-Bound Work**

If your program performs heavy calculations, **multiprocessing** can be a better choice.

### Simple code

```python
from multiprocessing import Process

def calculate():
    total = 0

    for i in range(1000000):
        total += i

    print("Calculation completed")

p1 = Process(target=calculate)
p2 = Process(target=calculate)

p1.start()
p2.start()

p1.join()
p2.join()

print("All processes completed")
```

### Output

```text
Calculation completed
Calculation completed
All processes completed
```

The order of the first two lines can vary.

### Why choose multiprocessing?

Each process has its own Python interpreter and memory space, allowing CPU-bound work to use multiple CPU cores.


**# 5. Simple Decision Example**

Suppose you are designing a program.

### Case 1: Download 100 files

```text
Downloading files
       ↓
Mostly waiting for network
       ↓
Threading / Asyncio
```

### Case 2: Process large images

```text
Image processing
       ↓
Heavy CPU calculations
       ↓
Multiprocessing
```

### Case 3: Web server handling thousands of connections

```text
Many network requests
       ↓
Mostly I/O waiting
       ↓
Asyncio
```

---

**# Algorithm for Choosing a Concurrency Model**

1. Identify the type of task.
2. Check whether the task is **CPU-bound or I/O-bound**.
3. If it is a simple program, use sequential execution.
4. If it is I/O-bound with relatively simple threaded tasks, consider **threading**.
5. If there are many concurrent I/O operations, consider **asyncio**.
6. If it is CPU-bound, consider **multiprocessing**.
7. Consider memory usage, complexity, and synchronization requirements.
8. Test the chosen model with realistic workloads.

**To choose a concurrency model, first determine whether the application is CPU-bound or I/O-bound. Threading is suitable for I/O-bound tasks where operations spend time waiting. Asyncio is suitable for handling many asynchronous I/O operations efficiently. Multiprocessing is suitable for CPU-bound tasks because separate processes can use multiple CPU cores. For simple tasks with little concurrency, sequential execution is sufficient.**

**I/O → Threading/Asyncio**
**CPU → Multiprocessing**
**Simple → Sequential**


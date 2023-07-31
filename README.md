# Pretty Asyncio
pretty asyncio is a library to ease the usage of the built in `asyncio` library by providing simple decorators.


## Usage
**Using Normal Asyncio**
```python
import asyncio

async def long_process():
    await asyncio.sleep(5)
    return '(e.g. data from IO process)'

def sync_operation():
    print('sync operation')

async def main():
    # Run the corutine as a task
    task = asyncio.create_task(long_process())
    
    sync_operation()

    await task
    print(task.result())

asyncio.run(main())
```
**Using Pretty Asyncio**
```python
from pasyncio import run, create_task

@create_task
async def long_process():
    await asyncio.sleep(5)
    return '(e.g. data from IO process)'

def sync_operation():
    print('sync operation')

@run
async def main():
    long_process()

    sync_operation()

main()
```

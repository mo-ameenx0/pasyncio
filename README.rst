# Pretty Asyncio
pretty asyncio is a library to ease the usage of the built in `asyncio` library by providing simple decorators.


## Usage
**Using Normal Asyncio**
```python
import asyncio

async def long_process():
    await asyncio.sleep(5)
    return '(e.g. data from IO process)'

async def main():
    result = await asyncio.create_task(long_process())

    print(result)

asyncio.run(main())
```
**Using Pretty Asyncio**
```python
import asyncio
from pasyncio import run, create_task

@create_task
async def long_process():
    await asyncio.sleep(5)
    return '(e.g. data from IO process)'

@run
async def main():
    result = await long_process()

    print(result)

main()
```

## Installation

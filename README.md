# Pretty Asyncio
Pretty Asyncio goal is to ease the usage of the built in `asyncio` library by providing simple python 
decorators. `pasyncio` doesn't add new features to the existing library but only provides a simpler way to use `asyncio` 
library.

## Hello World
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

## Rational
When using python `asyncio` to create a non-blocking application it feels like something new and hard to grasp from the 
first time. You need to understand how to run your program in an event loop so you can start creating coroutines by 
adding `async` to your methods. Then you need to create tasks or ensure futures so your coroutines can be scheduled 
to be run by the event loop. As it gets hard to understand the concept, it gets harder to follow the code. Imagine 
writing for every `async` method in your code a couple of lines just to initiate the code and start using the library.

For a quick comparison between a non-blocking language like `javascript` and python `asyncio` we can see the problem.

```javascript
async function getData() {
    console.log('get data from server')
}

async function readFile() {
    console.log('read file')
}

await getData()
await readFile()
```
This is a simple `async` method in `javascript` nothing new! Now let us see the same program in python.

```python
import asyncio

async def getData():
    print('get data from server')

async def readFile():
    print('read file')

loop = asyncio.get_event_loop()

tasks = [
    loop.create_task(getData()),
    loop.create_task(readFile())
]

loop.run_until_complete(
    asyncio.wait(tasks)
)
```

I think now after this simple comparison the issue is visible. python requires so much to run asynchronous programs. However, 
the previous python example could be modified more to make it easier to read.

```python
from asyncio import run, create_task

async def getData():
    print('get data from server')

async def readFile():
    print('read file')

async def main():
    await create_task(getData())
    await create_task(readFile())

run(main())
```

Ok much better! however, for this simple program it start to be overwhelming to add a new `async`. The comparison goal 
is just to see how clear the `javascript` async/await compared to python when using `asyncio`.

Now, `pasyncio` want to achive this simplicity in the code. Let's us see how `pasyncio` achive more code readability.

```python
from pasyncio import run, create_task

@create_task
async def getData():
    print('get data from server')

@create_task
async def readFile():
    print('read file')

@run
async def main():
    await getData()
    await readFile()

main()
```

Much better, now it is easier to follow the code.

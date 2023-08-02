import asyncio
from functools import wraps
from inspect import iscoroutinefunction

def run(func=None, *, debug=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not iscoroutinefunction(func):
                raise TypeError(f'the decorated function ({func.__name__}) is not a coroutine use async')

            asyncio.run(
                func(*args, **kwargs),
                debug=debug
            )

        return wrapper
    if callable(func):
        return decorator(func)
    return decorator

def run_until_complete(func=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not iscoroutinefunction(func):
                    raise TypeError(f'the decorated function ({func.__name__}) is not a coroutine use async')

            loop = asyncio.get_event_loop()
            loop.run_until_complete(func())

        return wrapper
    if callable(func):
        return decorator(func)
    return decorator

def run_forever(func=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not iscoroutinefunction(func):
                raise TypeError(f'the decorated function ({func.__name__}) is not a coroutine use async')
            
            loop = asyncio.get_event_loop()
            asyncio.ensure_future(func())
            loop.run_forever()

        return wrapper
    if callable(func):
        return decorator(func)
    return decorator

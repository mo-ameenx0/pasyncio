import asyncio
from functools import wraps
from inspect import iscoroutinefunction

def create_task(func=None, *, name=None, context=None, callback=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not iscoroutinefunction(func):
                raise TypeError(f'the decorated function ({func.__name__}) is not a coroutine use async')

            if not callback and not callable(callback):
                raise TypeError(f'the callback for function ({func.__name__}) must be callable not a {type(callback)}')

            task = asyncio.create_task(
                func(*args, **kwargs), 
                name=name,
                context=context
            )

            if callable(callback):
                task.add_done_callback(
                    callback,
                    context=context
                )
            
            return task

        return wrapper
    if callable(func):
        return decorator(func)
    return decorator

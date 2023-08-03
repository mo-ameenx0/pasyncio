import asyncio
from functools import wraps

def call_soon(func=None, *, callback, context=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not callback and not callable(callback):
                raise TypeError(f'the callback for function ({func.__name__}) must be callable not a {type(callback)}')

            loop = asyncio.get_event_loop()
            loop.call_soon(
                callback,
                args,
                context=context,
            )

            func(*args, **kwargs)

        return wrapper
    if callable(func):
        return decorator(func)
    return decorator

def call_later(func=None, *, delay, callback, context=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not callback and not callable(callback):
                raise TypeError(f'the callback for function ({func.__name__}) must be callable not a {type(callback)}')

            loop = asyncio.get_event_loop()
            loop.call_later(
                delay,
                callback,
                args,
                context=context,
            )

            func(*args, **kwargs)

        return wrapper
    if callable(func):
        return decorator(func)
    return decorator

def call_at(func=None, *, when, callback, context=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not callback and not callable(callback):
                raise TypeError(f'the callback for function ({func.__name__}) must be callable not a {type(callback)}')

            loop = asyncio.get_event_loop()
            loop.call_at(
                when,
                callback,
                args,
                context=context,
            )

            func(*args, **kwargs)

        return wrapper
    if callable(func):
        return decorator(func)
    return decorator

import asyncio
from threading import Thread
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
            loop.run_until_complete(func(*args, **kwargs))

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
            asyncio.ensure_future(func(*args, **kwargs))
            loop.run_forever()

        return wrapper
    if callable(func):
        return decorator(func)
    return decorator

def run_in_thread(func=None, *, debug=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not iscoroutinefunction(func):
                raise TypeError(f'the decorated function ({func.__name__}) is not a coroutine use async')

            def run_in_thread(loop):
                asyncio.set_event_loop(loop)
                asyncio.run(
                    func(*args, **kwargs),
                    debug=debug
                )

            Thread(
                target=run_in_thread,
                args=(asyncio.new_event_loop(),)
            ).start()

        return wrapper
    if callable(func):
        return decorator(func)
    return decorator


def run_until_complete_in_thread(func=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not iscoroutinefunction(func):
                raise TypeError(f'the decorated function ({func.__name__}) is not a coroutine use async')

            def run_in_thread(loop):
                asyncio.set_event_loop(loop)
                loop.run_until_complete(func(*args, **kwargs))
                
            Thread(
                target=run_in_thread,
                args=(asyncio.new_event_loop(),)
            ).start()
            
        return wrapper
    if callable(func):
        return decorator(func)
    return decorator

def run_forever_in_thread(func=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not iscoroutinefunction(func):
                raise TypeError(f'the decorated function ({func.__name__}) is not a coroutine use async')

            def run_in_thread(loop):
                asyncio.set_event_loop(loop)
                asyncio.ensure_future(func(*args, **kwargs))
                loop.run_forever()

            Thread(
                target=run_in_thread,
                args=(asyncio.new_event_loop(),)
            ).start()

        return wrapper
    if callable(func):
        return decorator(func)
    return decorator

import asyncio
from functools import wraps
from threading import Thread
from inspect import iscoroutinefunction

# ********* Runners *********
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


# ********* create_task *********
def create_task(func=None, *, name=None, context=None, callback=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not iscoroutinefunction(func):
                raise TypeError(f'the decorated function ({func.__name__}) is not a coroutine use async')

            if callback and not callable(callback):
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

# ********* Loop Callbacks *********
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

import timeit
from functools import wraps

def timerdec(consumer=lambda t: None):
    """Timer decorator factory."""
    def decorator(func):
        """Timer decorator,
        that tracks the execution time of the given function
        and applies the given consumer to the elapsed time in seconds."""
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = timeit.default_timer()
            r = func(*args, **kwargs)
            end = timeit.default_timer()
            consumer(end-start)
            return r
        return wrapper
    return decorator

if __name__ == '__main__':
    @timerdec(lambda t: print('Took', 1000*t, 'ms.'))
    def foo():
        for _ in range(1000000):
            pass
    foo()

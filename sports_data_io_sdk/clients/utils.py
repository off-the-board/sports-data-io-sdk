from functools import wraps


def ADD_AUTH(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        return {"url": func(self, *args, **kwargs), "params": self._params}
    return wrapper

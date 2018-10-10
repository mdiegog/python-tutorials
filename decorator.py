from functools import wraps

def debug(f):
    @wraps(f)
    def new_function(*args, **kwargs):
        print(f"Function {f.__name__}() called!")
        return f(*args, **kwargs)
    return new_function

@debug
def neg(n):
    """Retorna el inverso de n."""
    return n * -1
print(neg.__name__)  # new_function
help(neg)

print(neg(-1))

from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return  fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(40))

print(fibonacci(40))
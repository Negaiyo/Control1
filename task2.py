# Напишите осмысленный декоратор.
def rev(func):
    def wrapper():
        original = func()
        modified = original[::-1]
        return modified
    return wrapper

@rev
def function():
    return "Hello"

print(function())


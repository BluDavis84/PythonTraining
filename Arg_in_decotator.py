from rich import print as rprint

def politeness(func):
    def wrapper(*args , **kwargs):
        rprint("some stuff")
        func(*args , **kwargs)
        rprint("more stuff")
        return wrapper
    
@politeness
def new(n , b):
    print(n+b)

new(19,20)
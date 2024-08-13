from rich import print as rprint

def prettify(func):
    def wrapper():
        rprint("^^^^^^^^^^^^^^^^^^")
        func()
        rprint("******************")
    return wrapper

@prettify # <----- this makes decotaters easler to code. Look at the first one to understand what I'm talking about
def banner():
    print("Do not access the device")

banner()


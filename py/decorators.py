def announce(f):
    def wrapper():
        print("About to call the function...")
        f()
        print("Function has been called.")
    return wrapper

@announce
def greet():
    print("Hello, World!")

greet()
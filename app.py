def greet(name):
    return f"Hello, {name}! This is running inside Docker."

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))


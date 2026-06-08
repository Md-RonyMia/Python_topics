class Greeting:
    def __call__(self,name):
        #returns a greeting message that includes the provided name when the object of the class is called as a function
        return f"Hello, {name}!"
greet = Greeting()
print(greet("Alice"))  # Output: Hello, Alice!
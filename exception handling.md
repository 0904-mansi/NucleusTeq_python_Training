# Exception Handling in Python

Exception handling in Python allows you to gracefully manage errors and unexpected situations that may occur during program execution. Python provides constructs such as try, except, finally, and raise for handling exceptions effectively.
Handling Exceptions with try and except

The try block allows you to write code that might raise an exception. The except block catches and handles specific exceptions that occur within the try block.

```python

try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handling a specific exception
    print("Error: Division by zero!")
```

# Handling Multiple Exceptions

You can handle multiple exceptions by specifying multiple except blocks or using a tuple in a single except block.

```python

try:
    # Code that may raise an exception
    result = int(input("Enter a number: ")) / 0
except ZeroDivisionError:
    print("Error: Division by zero!")
except ValueError:
    print("Error: Invalid input!")
```

# Handling Any Exception

You can catch any exception using a generic except block without specifying the type of exception.

```python

try:
    # Code that may raise an exception
    result = int(input("Enter a number: ")) / 0
except:
    print("An error occurred!")
```

# Executing Code After try-except

You can include a finally block to execute code regardless of whether an exception occurred or not.

```python

try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")
finally:
    # Code that will always execute
    print("Execution complete.")
```

# Raising Exceptions with raise

You can raise exceptions manually using the raise statement. This allows you to indicate that an error condition has occurred.

```python

def sqrt(x):
    if x < 0:
        raise ValueError("Square root of negative number is undefined.")
    else:
        return x ** 0.5

try:
    print(sqrt(-1))
except ValueError as ve:
    print(ve)
```

# Custom Exceptions

You can define custom exception classes by inheriting from the Exception class.

```python

class CustomError(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise CustomError("This is a custom exception.")
except CustomError as ce:
    print(ce.message)
```

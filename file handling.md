# File Handling in Python
### Opening a File

You can open a file in Python using the open() function. The syntax is:
```python
file_object = open(filename, mode)
```
filename: The name of the file you want to open.
mode: Specifies the purpose of opening the file (read, write, append, etc.). It's an optional parameter, and if not specified, the default mode is 'r' (read mode).

# Modes for Opening a File

 - 'r': Read mode (default). Opens a file for reading. Throws an error if the file doesn't exist.
 - 'w': Write mode. Opens a file for writing. If the file exists, it truncates it. If not, it creates a new file.
 - 'a': Append mode. Opens a file for appending. If the file doesn't exist, it creates a new one.
 - 'b': Binary mode. Opens a file in binary mode.
 - 't': Text mode (default). Opens a file in text mode.
 - '+': Read/write mode. Opens a file for both reading and writing.

# Reading from a File

You can read the contents of a file using various methods such as read(), readline(), or readlines(). Here's how:

```python

# Reading entire file
content = file_object.read()

# Reading a single line
line = file_object.readline()

# Reading all lines into a list
lines = file_object.readlines()
```

# Writing to a File

To write to a file, you can use the write() method:

```python

file_object.write("Content to be written")
```
# Closing a File

After performing operations on a file, it's essential to close it using the close() method:

```python

file_object.close()
```
# Using with Statement

Python's with statement ensures that the file is properly closed after its suite finishes, even if an exception is raised. It simplifies the code and makes it more readable:

```python

with open(filename, mode) as file_object:
    # Perform file operations here
```
Example: Reading from a File

```python

with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```
Example: Writing to a File

```python

with open("example.txt", "w") as file:
    file.write("This is an example.")
```

# Open a file in append mode
```python
with open("example.txt", "a") as file:
    # Write content to the file
    file.write("\nNew content appended.")
```
These are the basics of file handling in Python. Remember to handle exceptions appropriately, especially when dealing with file operations.

```python
with open("image.jpg", "rb") as file:
    # Perform operations on the binary file
    # For example, read the first 10 bytes
    data = file.read(10)
    print(data)
```

Read chars

```python
# Open the file in read mode
with open("example.txt", "r") as file:
    # Read the first 2 characters
    first_two_chars = file.read(2)
    print("First 2 characters from the file:")
    print(first_two_chars)

```

```python
# Open a file in read/write mode
with open("example.txt", "r+") as file:
    # Read the contents of the file
    content = file.read()
    print("Contents of the file:")
    print(content)

    # Move the file pointer to the beginning
    file.seek(0)

    # Write additional content to the file
    file.write("\nAdditional content added.")

    # Move the file pointer to the beginning again
    file.seek(0)

    # Read the updated contents of the file
    updated_content = file.read()
    print("\nUpdated contents of the file:")
    print(updated_content)
```


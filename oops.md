# Object-Oriented Programming (OOP) in Python

## Four Pillars of OOP

### 1. Encapsulation

- **Definition:** Encapsulation is a process of wrapping data and methods in a single unit is called encapsulation. In OOP, data and methods operating on that data are combined together to form a single unit, which is referred to as a Class. The capsule, it is wrapped with different medicines. In a capsule, all medicine is encapsulated inside capsule.
- **Example:**
    ```python
    class BankAccount:
        def __init__(self, balance):
            self.balance = balance

        def deposit(self, amount):
            self.balance += amount

        def withdraw(self, amount):
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("Insufficient funds.")
    ```

### 2. Inheritance

- **Definition:** Allows a class (subclass) to inherit properties and behaviors from another class (superclass).
- **Example:**
    ```python
    class Animal:
        def speak(self):
            pass

    class Dog(Animal):
        def speak(self):
            return "Woof!"

    class Cat(Animal):
        def speak(self):
            return "Meow!"
    ```
# Inheritance in Object-Oriented Programming

Inheritance is a key concept in Object-Oriented Programming that allows a class to inherit properties and behaviors from another class. There are five types of inheritance:

## 1. Single Inheritance

- **Definition:** A class inherits from only one superclass.
- **Example:**
    ```python
    class Animal:
        def speak(self):
            pass

    class Dog(Animal):
        def bark(self):
            return "Woof!"
    ```

## 2. Multiple Inheritance

- **Definition:** A class inherits from more than one superclass.
- **Example:**
    ```python
    class A:
        def method_a(self):
            pass

    class B:
        def method_b(self):
            pass

    class C(A, B):
        def method_c(self):
            return "Combined functionality."
    ```

## 3. Multilevel Inheritance

- **Definition:** A class serves as a superclass for another class, creating a chain.
- **Example:**
    ```python
    class Animal:
        def speak(self):
            pass

    class Dog(Animal):
        def bark(self):
            return "Woof!"

    class GermanShepherd(Dog):
        def guard(self):
            return "Guarding the house."
    ```

## 4. Hierarchical Inheritance

- **Definition:** Multiple classes inherit from a single superclass.
- **Example:**
    ```python
    class Vehicle:
        def start(self):
            pass

    class Car(Vehicle):
        def drive(self):
            return "Car is moving."

    class Bike(Vehicle):
        def ride(self):
            return "Bike is moving."
    ```

## 5. Hybrid Inheritance

- **Definition:** A combination of two or more types of inheritance.
- **Example:**
    ```python
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B, C):
        pass
    ```

### 3. Polymorphism

- **Definition:**  Polymorphism refers to the process by which some code, data, method, or object behaves differently under different circumstances or contexts. Compile-time polymorphism and Run time polymorphism are the two types of polymorphisms in OOPs languages.

- **Example:**
    ```python
    def animal_sound(animal):
        return animal.speak()

    dog = Dog()
    cat = Cat()

    print(animal_sound(dog))  # Output: Woof!
    print(animal_sound(cat))  # Output: Meow!
    ```

  - **Method Overloading**: When there are multiple functions with the same name but different parameters then these functions are said to be overloaded. Functions can be overloaded by change in the number of arguments or/and a change in the type of arguments.
      ### Example:
```python
class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

# Usage
calc = Calculator()
print(calc.add(2, 3))       # Error: TypeError: add() missing 1 required positional argument: 'c'
print(calc.add(2, 3, 4))    # Output: 9

```

## Method Overriding 
Method overriding is one of the way by which java achieve Run Time Polymorphism.The version of a method that is executed will be determined by the object that is used to invoke it. If an object of a parent class is used to invoke the method, then the version in the parent class will be executed, but if an object of the subclass is used to invoke the method, then the version in the child class will be executed. In other words, it is the type of the object being referred to (not the type of the reference variable) that determines which version of an overridden method will be executed.
```python
class Animal:
    def sound(self):
        return "Animal makes a sound."

class Dog(Animal):
    def sound(self):
        return "Dog barks."

# Usage
animal = Animal()
dog = Dog()

print(animal.sound())   # Output: Animal makes a sound.
print(dog.sound())      # Output: Dog barks.
```
### 4. Abstraction

- **Definition:** Simplifying complex systems by providing a simple interface and hiding implementation details.
- **Example:**
    ```python
    from abc import ABC, abstractmethod

    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 3.14 * self.radius ** 2
    ```

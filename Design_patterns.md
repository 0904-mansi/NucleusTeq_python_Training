# What are Design Patterns?

Design patterns are basically defined as reusable solutions to the common problems that arise during software design and development. They are general templates or best practices that guide developers in creating well-structured, maintainable, and efficient code. 

![image](https://github.com/0904-mansi/Nucleus_Teq_python_Training/assets/81081105/0fbb534a-a667-4c81-bf33-9b36e27432d8)

# What is Singleton Method Design Pattern?

The Singleton method or Singleton Design pattern is one of the simplest design patterns. It ensures a class only has one instance, and provides a global point of access to it. 
```java
/*package whatever //do not write package name here */
import java.io.*;
public class Singleton {
    // static class
    private static Singleton instance;
    private Singleton()
    {
        System.out.println("Singleton is Instantiated.");
    }
    public static Singleton getInstance()
    {
        if (instance == null)
            instance = new Singleton();
        return instance;
    }
    public static void doSomething()
    {
        System.out.println("Somethong is Done.");
    }
    
    public static void main(String[] args)
    {
        Singleton.getInstance().doSomething();
        Singleton.getInstance().doSomething();
        
    }
}
```


# Factory method for designing pattern

The factory method is a creational design pattern, i.e., related to object creation. The Factory Method pattern is used to create objects without specifying the exact class of object that will be created. This pattern is useful when you need to decouple the creation of an object from its implementation.
```java
// Interface for vehicle
interface Vehicle {
    void printInfo();
}

// Concrete classes for different types of vehicles
class TwoWheeler implements Vehicle {
    public void printInfo() {
        System.out.println("I am a two wheeler");
    }
}

class ThreeWheeler implements Vehicle {
    public void printInfo() {
        System.out.println("I am a three wheeler");
    }
}

class FourWheeler implements Vehicle {
    public void printInfo() {
        System.out.println("I am a four wheeler");
    }
}

// Factory class to create vehicles
class VehicleFactory {
    Vehicle createVehicle(VehicleType type) {
        switch (type) {
            case VT_TwoWheeler:
                return new TwoWheeler();
            case VT_ThreeWheeler:
                return new ThreeWheeler();
            case VT_FourWheeler:
                return new FourWheeler();
            default:
                return null;
        }
    }
}

// Enum for vehicle types
enum VehicleType {
    VT_TwoWheeler,
    VT_ThreeWheeler,
    VT_FourWheeler
}

// Client class to use the factory and get vehicles
public class Main {
    public static void main(String[] args) {
        VehicleFactory factory = new VehicleFactory();

        Vehicle vehicle1 = factory.createVehicle(VehicleType.VT_TwoWheeler);
        vehicle1.printInfo();

        Vehicle vehicle2 = factory.createVehicle(VehicleType.VT_ThreeWheeler);
        vehicle2.printInfo();

        Vehicle vehicle3 = factory.createVehicle(VehicleType.VT_FourWheeler);
        vehicle3.printInfo();
    }
}
```
# Abstract Factory Pattern

Abstract Factory pattern is almost similar to Factory Pattern and is considered as another layer of abstraction over factory pattern. Abstract Factory patterns work around a super-factory which creates other factories.

# Builder Design Pattern

The Builder Design Pattern is a creational pattern used in software design to construct a complex object step by step. It allows the construction of a product in a step-by-step fashion,

# Components of the Builder Design Pattern

1. Product

The Product is the complex object that the Builder pattern is responsible for constructing.

2. Builder

The Builder is an interface or an abstract class that declares the construction steps for building a complex object.

3. ConcreteBuilder

ConcreteBuilder classes implement the Builder interface, providing specific implementations for building each part of the product.

4. Director

The Director is responsible for managing the construction process of the complex object.

5. Client

The Client is the code that initiates the construction of the complex object.

```java
// Product class
class Burger {
    private String bread;
    private String meat;
    private boolean cheese;
    private boolean lettuce;
    private boolean tomato;

    public Burger(String bread, String meat, boolean cheese, boolean lettuce, boolean tomato) {
        this.bread = bread;
        this.meat = meat;
        this.cheese = cheese;
        this.lettuce = lettuce;
        this.tomato = tomato;
    }

    @Override
    public String toString() {
        return "Burger{" +
                "bread='" + bread + '\'' +
                ", meat='" + meat + '\'' +
                ", cheese=" + cheese +
                ", lettuce=" + lettuce +
                ", tomato=" + tomato +
                '}';
    }
}

// Builder class
class BurgerBuilder {
    private String bread;
    private String meat;
    private boolean cheese;
    private boolean lettuce;
    private boolean tomato;

    public BurgerBuilder() {
    }

    public BurgerBuilder withBread(String bread) {
        this.bread = bread;
        return this;
    }

    public BurgerBuilder withMeat(String meat) {
        this.meat = meat;
        return this;
    }

    public BurgerBuilder withCheese(boolean cheese) {
        this.cheese = cheese;
        return this;
    }

    public BurgerBuilder withLettuce(boolean lettuce) {
        this.lettuce = lettuce;
        return this;
    }

    public BurgerBuilder withTomato(boolean tomato) {
        this.tomato = tomato;
        return this;
    }

    public Burger build() {
        return new Burger(bread, meat, cheese, lettuce, tomato);
    }
}

// Client class
public class Main {
    public static void main(String[] args) {
        // Using the builder to create a burger
        Burger burger = new BurgerBuilder()
                            .withBread("Wheat")
                            .withMeat("Beef")
                            .withCheese(true)
                            .withLettuce(true)
                            .withTomato(false)
                            .build();

        System.out.println(burger);
    }
}
```

# Prototype Design Pattern

The Prototype Design Pattern is a creational pattern that enables the creation of new objects by copying an existing object. Prototype allows us to hide the complexity of making new instances from the client. The concept is to copy an existing object rather than create a new instance from scratch, something that may include costly operations. The existing object acts as a prototype and contains the state of the object. 



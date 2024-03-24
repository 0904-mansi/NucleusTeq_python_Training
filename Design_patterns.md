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


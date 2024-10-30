package lab1;

public class Vehicle {
    // Attributes of the Vehicle
    private String color;
    private int age;          // In years
    private int power;        // Power in horsepower (HP)
    private int maxSpeed;     // Maximum speed in km/h
    private int currentSpeed; // Current speed in km/h
    private int x, y;         // Coordinates of the vehicle

    // Constructor
    public Vehicle(String color, int age, int power, int maxSpeed) {
        this.color = color;
        this.age = age;
        this.power = power;
        this.maxSpeed = maxSpeed;
        this.currentSpeed = 0; // Initially, the vehicle is stationary
        this.x = 0;            // Start at (0, 0)
        this.y = 0;
    }

    // Method to move the vehicle to a new set of coordinates (x, y)
    public void moveTo(int newX, int newY) {
        this.x = newX;
        this.y = newY;
        System.out.println("Vehicle moved to coordinates: (" + x + ", " + y + ")");
    }

    // Method to increase the speed of the vehicle
    public void increaseSpeed(int increment) {
        if (currentSpeed + increment <= maxSpeed) {
            currentSpeed += increment;
            System.out.println("Increased speed to: " + currentSpeed + " km/h");
        } else {
            currentSpeed = maxSpeed;
            System.out.println("Speed is at max: " + maxSpeed + " km/h");
        }
    }

    // Method to decrease the speed of the vehicle
    public void decreaseSpeed(int decrement) {
        if (currentSpeed - decrement >= 0) {
            currentSpeed -= decrement;
            System.out.println("Decreased speed to: " + currentSpeed + " km/h");
        } else {
            currentSpeed = 0;
            System.out.println("The vehicle has stopped.");
        }
    }

    // Getter and setter methods (if needed)
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public int getPower() {
        return power;
    }

    public void setPower(int power) {
        this.power = power;
    }

    public int getMaxSpeed() {
        return maxSpeed;
    }

    public void setMaxSpeed(int maxSpeed) {
        this.maxSpeed = maxSpeed;
    }

    public int getCurrentSpeed() {
        return currentSpeed;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    // Method to display vehicle details
    public void displayDetails() {
        System.out.println("Vehicle Details:");
        System.out.println("Color: " + color);
        System.out.println("Age: " + age + " years");
        System.out.println("Power: " + power + " HP");
        System.out.println("Max Speed: " + maxSpeed + " km/h");
        System.out.println("Current Speed: " + currentSpeed + " km/h");
        System.out.println("Current Position: (" + x + ", " + y + ")");
    }

    // Main method for testing
    public static void main(String[] args) {
        // Create a Vehicle object
        Vehicle car = new Vehicle("Red", 3, 150, 220);

        // Display initial details
        car.displayDetails();

        // Move the vehicle
        car.moveTo(10, 15);

        // Increase and decrease speed
        car.increaseSpeed(50);
        car.increaseSpeed(180);
        car.decreaseSpeed(30);
        car.decreaseSpeed(200);

        // Final vehicle details
        car.displayDetails();
    }
}

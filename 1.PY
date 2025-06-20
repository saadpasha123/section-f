// Online Java Compiler
// Use this editor to write, compile and run your Java code online

class PowerLaw {
    double current;
    double voltage;
    double power;

    // Constructor
    public PowerLaw(double current, double voltage) {
        this.current = current;
        this.voltage = voltage;
    }

    // Method to calculate power
    public void calculatePower() {
        power = current * voltage;
    }

    // Method to display power
    public void displayPower() {
        System.out.println("Power: " + power);
    }
}

public class Main {
    public static void main(String[] args) {
        // Create an instance of PowerLaw
        PowerLaw device = new PowerLaw(2.5, 12.0);

        // Calculate power
        device.calculatePower();

        // Display power
        device.displayPower();
    }
}

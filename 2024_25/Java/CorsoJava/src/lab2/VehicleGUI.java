package lab2;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class VehicleGUI extends JPanel implements ActionListener {
    private int x, y; // Position of the vehicle (point)
    private int currentSpeed; // Speed of the vehicle
    private Timer timer; // Timer for animation

    // Vehicle attributes
    private final int WIDTH = 800;
    private final int HEIGHT = 600;

    // GUI components
    private JButton increaseSpeedButton, decreaseSpeedButton, stopButton;
    private JTextField speedInputField;

    // Constructor
    public VehicleGUI() {
        // Initial vehicle attributes
        x = 50; // Start position
        y = HEIGHT / 2; // Vertical center
        currentSpeed = 0;

        // Set up the GUI
        this.setPreferredSize(new Dimension(WIDTH, HEIGHT));
        this.setBackground(Color.WHITE);

        // Create a timer to update vehicle position every 50ms
        timer = new Timer(50, this);
        timer.start();

        // Add control buttons and input field
        increaseSpeedButton = new JButton("Increase Speed");
        decreaseSpeedButton = new JButton("Decrease Speed");
        stopButton = new JButton("Stop Vehicle");
        speedInputField = new JTextField("Enter Speed", 10);

        increaseSpeedButton.addActionListener(e -> increaseSpeed());
        decreaseSpeedButton.addActionListener(e -> decreaseSpeed());
        stopButton.addActionListener(e -> stopVehicle());

        // Add components to the panel
        JPanel controlPanel = new JPanel();
        controlPanel.add(new JLabel("Speed Control:"));
        controlPanel.add(speedInputField);
        controlPanel.add(increaseSpeedButton);
        controlPanel.add(decreaseSpeedButton);
        controlPanel.add(stopButton);

        // Set layout and add control panel to the main panel
        this.setLayout(new BorderLayout());
        this.add(controlPanel, BorderLayout.SOUTH);
    }

    // Method to increase speed
    private void increaseSpeed() {
        try {
            int inputSpeed = Integer.parseInt(speedInputField.getText());
            currentSpeed += inputSpeed;
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(this, "Please enter a valid number!");
        }
    }

    // Method to decrease speed
    private void decreaseSpeed() {
        try {
            int inputSpeed = Integer.parseInt(speedInputField.getText());
            currentSpeed -= inputSpeed;
            if (currentSpeed < 0) {
                currentSpeed = 0; // Ensure speed doesn't go negative
            }
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(this, "Please enter a valid number!");
        }
    }

    // Method to stop the vehicle
    private void stopVehicle() {
        currentSpeed = 0;
    }

    // Action event called by the Timer to update vehicle position
    @Override
    public void actionPerformed(ActionEvent e) {
        x += currentSpeed / 10; // Move the vehicle based on speed

        // Keep the vehicle within the screen bounds
        if (x > WIDTH) {
            x = 0; // Loop back to the start when it reaches the end
        }

        // Repaint the panel (this will trigger the paintComponent method)
        repaint();
    }

    // Paint method to display the vehicle (as a point)
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        // Draw the vehicle as a small circle (point)
        g.setColor(Color.RED);
        g.fillOval(x, y, 20, 20); // The vehicle is represented as a circle
    }

    // Main method to create and display the window
    public static void main(String[] args) {
        JFrame frame = new JFrame("Vehicle Simulation");
        VehicleGUI vehiclePanel = new VehicleGUI();

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(vehiclePanel);
        frame.pack();
        frame.setVisible(true);
    }
}


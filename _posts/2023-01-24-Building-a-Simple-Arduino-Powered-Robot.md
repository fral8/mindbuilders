---
layout: single
title:  Building a Simple Arduino-Powered Robot
categories:
  - tutorial
  - maker
  - arduino
share: true
excerpt: "Building a Simple Arduino-Powered Robot: A Step-by-Step Guide with Real Materials and Prices."
header:
    teaser: /assets/images/arduinorobot.jpg
    overlay_image: /assets/images/arduinorobot.jpg
    overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
toc: true


---
## Intro
Building your own robot can be a fun and rewarding experience. With the help of an Arduino microcontroller, you can create a robot that can move, sense its environment, and even make decisions. In this tutorial, we'll be building a simple robot that can move in different directions based on sensor input.

## Shopping-list
1. [Arduino Uno](https://amzn.to/3w8O0BL) -  around $25
2. [2 DC motors](https://amzn.to/3ITBHAV) - around $10 for a pair
3. [L298N Dual H-Bridge Motor Driver](https://amzn.to/3Wbyhg1) - around $10
4. [Breadboard and Jumper Wires](https://amzn.to/3iMBQeY) - around $15
5. [2 plastic wheels with diameter of 50mm](https://www.amazon.com/dp/B07M7ZJ6Z5/) - around $10 for a pair
6. [2 ball casters](https://www.amazon.com/dp/B07MCVRZS5/) - around $7 for a pair
7. [2 Sharp GP2Y0A02YK0F infrared proximity sensor](https://amzn.to/3w9dbnR)

## Step 1: Setting up the Hardware

The first step in building your robot is to set up the hardware. Start by connecting the motors and motor driver to the breadboard. In this example, we will be using a L298N Dual H-Bridge Motor Driver. This motor driver is capable of controlling the speed and direction of the motors. Connect the DC motors to the OUT1 and OUT2 pins of the motor driver. Make sure to connect the motors to the correct pins on the motor driver, as this will determine the direction in which the robot moves.

Next, connect the power supply to the breadboard. Connect the positive rail of the breadboard to the VCC pin of the motor driver, and the negative rail to the GND pin. This will provide power to the motors.

Finally, connect the Arduino to the breadboard. Use jumper wires to connect the breadboard to the digital pins of the Arduino that will be used to control the motor driver. In this example, we will be using pins 8, 9, 10 and 11.

With this setup, you have the basic hardware for your robot. Now you can proceed to the next step and wire the sensors.

## Step 2: Wiring the Sensors

Next, wire the infrared sensors to the breadboard. These sensors will be used to detect obstacles in the robot's path. In this example, we will be using Sharp GP2Y0A02YK0F infrared proximity sensor.

Connect the Vcc pin of the sensor to the 5V pin of the Arduino and Gnd pin to the Gnd pin of the Arduino. Connect the output pin of the sensor to one of the digital pin of the Arduino, for example, pin 2. Repeat the same process for the second sensor, and connect it to another digital pin, for example, pin 3.

With this setup, you have the basic hardware for your robot and the sensors are connected and ready to use. Now you can proceed to the next step and write the code that will control the robot.

## Step 3: Writing the Code

Now that the hardware is set up, it's time to write the code that will control the robot. Start by defining the pins that the motors and sensors are connected to. In this example, the left motor is connected to OUT1 and OUT2 of the L298N motor driver, the right motor is connected to OUT3 and OUT4, the left sensor is connected to digital pin 2 and the right sensor is connected to digital pin 3.

Then, create variables to store the sensor readings. In the loop() function, use the analogRead() function to read the sensor values and store them in variables. Use the map() function to convert the sensor readings to a range that is more suitable for your application. In this case, we will map the sensor readings from 0 to 1023 to a range of 0 to 255.

Next, use the sensor readings to determine the direction in which the robot should move. For example, if the left sensor detects an obstacle, the robot should turn to the right. To do this, use if-else statements to check the sensor readings and use the digitalWrite() function to control the motor driver pins.

Here is a sample code:

'''
const int leftMotorOut1 = 8;
const int leftMotorOut2 = 9;
const int rightMotorOut1 = 10;
const int rightMotorOut2 = 11;
const int leftSensorPin = 2;
const int rightSensorPin = 3;

void setup() {
  pinMode(leftMotorOut1, OUTPUT);
  pinMode(leftMotorOut2, OUTPUT);
  pinMode(rightMotorOut1, OUTPUT);
  pinMode(rightMotorOut2, OUTPUT);
  pinMode(leftSensorPin, INPUT);
  pinMode(rightSensorPin, INPUT);
}

void loop() {
  int leftSensorValue = map(analogRead(leftSensorPin), 0, 1023, 0, 255);
  int rightSensorValue = map(analogRead(rightSensorPin), 0, 1023, 0, 255);

  if (leftSensorValue > 100) {
    digitalWrite(leftMotorOut1, HIGH);
    digitalWrite(leftMotorOut2, LOW);
    digitalWrite(rightMotorOut1, LOW);
    digitalWrite(rightMotorOut2, HIGH);
  } else if (rightSensorValue > 100) {
    digitalWrite(leftMotorOut1, LOW);
    digitalWrite(leftMotorOut2, HIGH);
    digitalWrite(rightMotorOut1, HIGH);
    digitalWrite(rightMotorOut2, LOW);
  }
}
'''
With this code, you have the basic control of the robot. The robot will move forward if neither of the sensors detect any obstacles, and will turn right or left if one of the sensors detects an obstacle. You can adjust the threshold value of 100 and tweak the code to suit your needs.

## Step 4: Assembling the Robot

Once you have the code working, it's time to assemble the robot. Start by attaching the wheels and ball casters to the motors. In this example, we will be using two plastic wheels with a diameter of 50mm and two ball casters. These components can be purchased separately or as a kit.

Then, attach the breadboard and Arduino to the robot's chassis. You can use acrylic or cardboard to make the robot's chassis. Make sure to leave enough room for the components, sensors, and wiring. You can use double-sided tape or screws to secure the breadboard and Arduino to the chassis.

Finally, connect the motors to the motor driver and connect the power supply to the breadboard. Make sure everything is securely fastened and that the sensors are facing the front of the robot.

You can refer to this link to see an example of a robot made with acrylic: https://www.instructables.com/id/Acrylic-Chassis-Robot-with-Arduino-Uno/

With this setup, your robot is now ready to move and sense its environment. You can now proceed to the next step, testing and troubleshoot.

## Step 5: Testing and Troubleshooting

Finally, it's time to test the robot and troubleshoot any issues that may arise. Connect the Arduino to your computer using a USB cable and upload the code to the Arduino using the Arduino IDE software. Power on the robot by connecting a 9V battery or a power supply with the correct voltage to the breadboard.

Observe the robot's behavior and make adjustments to the code as needed. If the robot is not moving as expected, make sure that the motor connections are correct and that the sensor values are being read correctly. Use the serial monitor in the Arduino IDE to check the sensor values and debug the code if necessary.

You can also test the robot's sensors by placing an object in front of it, the robot should detect the object and change its direction.

In case of any issues, you can refer to the datasheet of the components you are using, for example, the L298N motor driver datasheet, the Sharp GP2Y0A02YK0F infrared proximity sensor datasheet, and the Arduino Uno datasheet for more information about the pinout and specifications.

With this simple Arduino-powered robot, you can now explore the world of robotics and get a taste of the possibilities that these technologies can offer. You can also use this robot as a starting point for more complex projects and add more sensors, actuators, and functions.

## Outro
With this simple Arduino-powered robot, you can now explore the world of robotics and get a taste of the possibilities that these technologies can offer. You can also use this robot as a starting point for more complex projects and add more sensors, actuators, and functions.
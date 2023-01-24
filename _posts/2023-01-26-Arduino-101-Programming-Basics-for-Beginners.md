---
layout: single
title:  Arduino 101- Programming Basics for Beginners
categories:
  - tutorial
  - maker
  - arduino
share: true
excerpt: "Learn the basics of programming with Arduino and create interactive projects"
header:
    teaser: /assets/images/arduino101.jpg
    overlay_image: /assets/images/arduino101.jpg
    overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
toc: true


---
## Intro
Arduino is a popular open-source microcontroller platform that allows users to create interactive electronic projects. Whether you're a beginner or an experienced maker, Arduino is a great tool to learn about programming and electronics.

In this guide, we'll cover the basics of programming with Arduino, including how to set up your development environment, how to upload code to an Arduino board, and how to write simple programs using the Arduino programming language.

## Shopping-list
Before we get started, you'll need to gather a few supplies:
1. [Arduino board](https://amzn.to/3H7D4uz) (such as the Arduino Uno): $24.95 
2. A USB cable to connect the Arduino to your computer
3. A computer with the Arduino IDE (Integrated Development Environment) software installed. You can download the Arduino IDE for free from the Arduino website.
nce you have all the necessary equipment, you're ready to start programming your Arduino.
## Step 1: Setting up the development environment
The first step is to set up the development environment by installing the Arduino IDE on your computer and connecting the Arduino board to your computer via the USB cable. Once the Arduino is connected, open the Arduino IDE and select the correct board type and serial port from the tools menu.

## Step 2: Uploading a program
The next step is to upload a program to the Arduino board. The Arduino IDE includes several example programs that you can use to test your board and make sure everything is working properly. To upload a program, simply open the program in the Arduino IDE and click the upload button. The program will be transferred to the Arduino board, where it will begin running.
## Writing your own program
Once you've got the basics down, it's time to start writing your own programs. The Arduino programming language is based on C++ and is relatively simple to learn. The language includes a variety of built-in functions and libraries that can be used to control the board's inputs and outputs, read data from sensors, and communicate with other devices.
Here are a few examples to help you get started:

### Blink an LED: 
This is a classic Arduino example that demonstrates how to control the digital output pins to blink an LED. The code will turn on the LED for a second, and then turn it off for a second, creating a blinking effect.
'''
void setup() {
  pinMode(13, OUTPUT); //sets pin 13 as an output
}

void loop() {
  digitalWrite(13, HIGH); //turns the LED on
  delay(1000); //waits for 1 second
  digitalWrite(13, LOW); //turns the LED off
  delay(1000); //waits for 1 second
}

'''

### Fading an LED
This example shows how to use PWM (pulse-width modulation) to fade an LED. The code uses the analogWrite() function to change the brightness of the LED.
'''
void setup() {
  pinMode(9, OUTPUT); //sets pin 9 as an output
}

void loop() {
  for (int i = 0; i <= 255; i++) {
    analogWrite(9, i); //fades the LED on
    delay(10);
  }
  for (int i = 255; i >= 0; i--) {
    analogWrite(9, i); //fades the LED off
    delay(10);
  }
}

'''
### Reading a potentiometer
This example shows how to read the value of a potentiometer (variable resistor) and use it to control the brightness of an LED.
'''
void setup() {
  pinMode(9, OUTPUT); //sets pin 9 as an output
  pinMode(A0, INPUT); //sets pin A0 as an input
}

void loop() {
  int potentiometer = analogRead(A0); //reads the value of the potentiometer
  int ledBrightness = map(potentiometer, 0, 1023, 0, 255); //maps the potentiometer value to a value between 0 and 255
  analogWrite(9, ledBrightness); //sets the brightness of the LED
}

'''
### Controlling a servo motor
This example shows how to use the Servo library to control a servo motor. The code uses the servo.attach() function to attach the servo to a specific pin, and the servo.write() function to set the position of the servo.
'''
#include <Servo.h>

Servo myservo;

void setup() {
  myservo.attach(9);
}

void loop() {
  for (int i = 0; i <= 180; i++) {
    myservo.write(i);
    delay(15);
  }
  for (int i = 180; i >= 0; i--) {
    myservo.write(i);
    delay(15);
  }
}

'''
## Outro

Arduino is a great tool for beginners to learn about programming and electronics. This guide provides an overview of the basics of programming with Arduino and provides a simple example to get you started. There are many resources available to help you learn more about programming with Arduino, such as the official Arduino website and online tutorials. With a little bit of practice and patience, you'll be able to create your own interactive projects with Arduino in no time!
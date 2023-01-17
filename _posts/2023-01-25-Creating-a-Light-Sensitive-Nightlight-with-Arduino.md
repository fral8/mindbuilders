---
layout: single
title:  Creating a Light-Sensitive Nightlight with Arduino
categories:
  - tutorial
  - maker
  - arduino
share: true
excerpt: "Learn how to create a energy-saving light-sensitive nightlight with Arduino in a few easy steps"
header:
    teaser: /assets/images/nightlightsensor.jpg
    overlay_image: /assets/images/nightlightsensor.jpg
    overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
toc: true
date: 2023-01-25 14:00:00

---
## Intro
Creating a light-sensitive nightlight with Arduino is a fun and easy project that can be completed in just a few hours. This nightlight will automatically turn on when the ambient light in the room drops below a certain level, and turn off when the light level increases. It's a great way to save energy and create a more pleasant sleeping environment.

## Shopping-list
1. Arduino board (such as the Arduino Uno): $24.95 - https://amzn.to/3H7D4uz
2. LDR (light-dependent resistor): $4.99 - https://amzn.to/3iLqxnc
3. Resistor (10k ohm resistor): $5.99 - https://amzn.to/3GJxnl7
4. LED (light-emitting diode): $5.99 - https://amzn.to/3XDujxC
5. Jumper wires & Breadboard: $15.99 - https://amzn.to/3GTlXLQ

## Step 1: Wiring the Hardware

First, let's set up the hardware. Connect the LDR to the breadboard, with one leg in the GND (ground) rail and the other leg in the A0 (analog input 0) pin on the Arduino. Connect the resistor between the LDR and the A0 pin. Then, connect the LED to the breadboard, with the positive leg in the D13 (digital output 13) pin on the Arduino, and the negative leg in the GND rail.

## Step 2: Writing Code

Next, we'll need to upload some code to the Arduino board. You can find the code on the Arduino website, or you can copy and paste the following code into the Arduino IDE (Integrated Development Environment):
'''
int ledPin = 13;
int ldrPin = A0;
int ldrValue = 0;

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  ldrValue = analogRead(ldrPin);
  if (ldrValue < 250) {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }
}
'''
This code tells the Arduino to read the value of the LDR and compare it to a threshold value of 250. If the value is less than 250, the LED will turn on, and if the value is greater than 250, the LED will turn off. You can adjust the threshold value to suit your own preferences.


## Step 3: Testing and Troubleshooting

Once you have uploaded the code to the Arduino, you can test your nightlight by dimming the lights in the room and watching the LED turn on. Congratulations, you've just made your own light-sensitive nightlight!

## Outro

If you're looking for a fun and easy DIY project, creating a light-sensitive nightlight with Arduino is a great choice. This project is perfect for beginners, and it's a great way to learn about how Arduino works and how to work with different types of components. Feel free to customize it to suit your needs and preferences. Happy making!
---
layout: single
title:  Connecting Sensors to an Arduino for Data Collection
categories:
  - tutorial
  - maker
  - arduino
share: true
excerpt: "Connect a photoresistor sensor to Arduino and use MongoDB for data collection and visualization with this step-by-step tutorial"
header:
    teaser: /assets/images/mongodb.png
    overlay_image: /assets/images/mongodb.png
    overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
toc: true
date: 2023-01-27 14:00:00

---
## Intro
In this tutorial, we will show you how to connect a photoresistor sensor to an Arduino board and use it to collect data. We will also cover how to use the MongoDB database to store and visualize the data.

## Shopping-list
Before we get started, you'll need to gather a few supplies:
1. Arduino board (such as the Arduino Uno): $24.95 - https://amzn.to/3H7D4uz
2. A USB cable to connect the Arduino to your computer
3. A computer with the Arduino IDE (Integrated Development Environment) software installed. You can download the Arduino IDE for free from the Arduino website.
nce you have all the necessary equipment, you're ready to start programming your Arduino.
4. LDR (light-dependent resistor): $4.99 - https://amzn.to/3iLqxnc
5. Resistor (10k ohm resistor): $5.99 - https://amzn.to/3GJxnl7
6. Jumper wires & Breadboard: $15.99 - https://amzn.to/3GTlXLQ

## Step 1: Connecting the sensor to the Arduino
- Begin by placing the photoresistor sensor on the breadboard. Connect one leg of the sensor to the GND rail and the other leg to the A0 pin on the Arduino.
- Next, place the 10K Ohm resistor between the A0 pin and the GND rail. This will act as a pull-down resistor, ensuring that the A0 pin has a known value when the sensor is not receiving light.
- Use the jumper wires to connect the breadboard to the Arduino board. Connect the GND rail to the GND pin on the Arduino, the + rail to the 5V pin, and the A0 pin to the A0 pin on the Arduino.

## Step 2: Writing the Arduino code

- Open the Arduino IDE on your computer and create a new sketch.
- In the setup() function, use the pinMode() function to set the A0 pin as an INPUT.
- In the loop() function, use the analogRead() function to read the value from the A0 pin and store it in a variable.
- Use the Serial.begin() function to start the serial communication and Serial.println() function to send the value to the serial monitor.
'''
void setup() {
  pinMode(A0, INPUT);
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(A0);
  Serial.println(sensorValue);
  delay(1000);
}

'''
- Upload the code to the Arduino board.
- Open the serial monitor and check that the value is changing when you cover or uncover the sensor.
## Step 3: Setting up MongoDB

- Install MongoDB on your computer by following the instructions provided on the [MongoDB website](https://www.mongodb.com/docs/manual/installation/).
- Create a new database and collection to store the sensor data.
- Install the MongoDB library for Arduino by going to Sketch > Include Library > MongoDB.
## Step 4: Integrating MongoDB with Arduino

- In the Arduino sketch, include the MongoDB library at the top of the code.
'''
#include <MongoDb.h>
'''
- Create a MongoDb object and establish a connection to the database.

'''
MongoDb mongodb;
mongodb.connect("mongodb://<hostname>:<port>/<database>");
'''
- In the loop() function, use the mongodb.insert() function to insert the sensor value into the database collection.
'''
mongodb.insert("<collection>", "{\"value\":\"" + String(sensorValue) + "\"}");
'''
- Upload the code to the Arduino board.
## Step 5: Visualizing the data

Use a MongoDB visualization tool, such as MongoDB Compass, to view the data stored in the database collection.
You can also create a simple web application to display the data in real-time using a library like Chart.js and connecting it to the MongoDB database.
## Outro
By following these steps, you should now have a working setup for collecting data from a photoresistor sensor using an Arduino board and storing it in a MongoDB database. This can be easily adapted for other sensors and expanded for more complex projects. Have fun collecting and analyzing data!
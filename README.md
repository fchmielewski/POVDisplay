# POV Display Project

This repository contains the design and implementation of a Persistence of Vision (POV) display that utilizes the POV effect to create the illusion of a stable image. The project involves both hardware and software components.

## Table of Contents

- [About the Project](#about-the-project)
- [Hardware](#hardware)
- [Software](#software)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## About the Project

The POV display project aims to create a prototype device capable of displaying colored images by rapidly displaying small image fragments in a specific sequence. The device consists of a rotating element with LEDs, a control system, and the necessary electronics to synchronize the LED display with the rotation.

## Hardware

The hardware component of the project includes:

- A brushless DC motor (Redox DC 12V 12000RPM)
- A motor controller
- A wireless power receiver module (DFRobot Wireless Charging Module 5V/5A)
- A Hall effect sensor (TLE4906L)
- An LED strip (Adafruit DotStar Digital LED Strip)
- A microcontroller board (Arduino Nano ESP32)
- A L7805CV voltage regulator 

## Software

The software component consists of two parts:

1. **Image Converter**: A Python script that converts an input image file into a format suitable for display on the POV device. The script remaps the pixels within the central circle of the input image and generates an array of RGB values for the microcontroller.

2. **Microcontroller Code**: An Arduino program that controls the LED strip and synchronizes the display with the rotation of the device. It utilizes the Hall effect sensor to detect the rotation and calculates the appropriate timing for displaying each image fragment.

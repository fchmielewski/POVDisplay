# POV Display Project

This repository contains the design and implementation of a Persistence of Vision (POV) display that utilizes the POV effect to create the illusion of a stable image. The project was created as a part of my Bachelor's of Engineering thesis.

## Table of Contents

- [About the Project](#about-the-project)
- [Hardware](#hardware)
- [Software](#software)
- [Example images](#example-images)
- [License](#license)

## About the Project

The POV display project aims to create a prototype device capable of displaying colored images by rapidly displaying small image fragments in a specific sequence. The device consists of a rotating element with LEDs, a control system, and the necessary electronics to synchronize the LED display with the rotation.

## Hardware

The hardware component of the project includes:

- Brushless DC motor (Redox DC 12V 12000RPM)
- Motor controller
- Wireless power receiver module (DFRobot Wireless Charging Module 5V/5A)
- Hall effect sensor (TLE4906L)
- LED strip (Adafruit DotStar Digital LED Strip)
- Microcontroller board (Arduino Nano ESP32)
- L7805CV voltage regulator

![display hardware diagram](https://github.com/fchmielewski/POVDisplay/blob/main/diagram.png)

## Software

The software component consists of two parts:

1. **Image Converter**: A Python script that converts an input image file into a format suitable for display on the POV device. The script remaps the pixels within the central circle of the input image and generates an array of RGB values for the microcontroller.

2. **Microcontroller Code**: An Arduino program that controls the LED strip and synchronizes the display with the rotation of the device. It utilizes the Hall effect sensor to detect the rotation and calculates the appropriate timing for displaying each image fragment.

## Example images
![demo image 1](https://github.com/fchmielewski/POVDisplay/blob/main/demo_images/demo1.jpeg)
![demo image 2](https://github.com/fchmielewski/POVDisplay/blob/main/demo_images/demo2.jpeg)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

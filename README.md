# Communication-between-Raspberry-pi-and-Android-Phone-app-BlueTerm

Raspberry Pi is very popular for IoT projects because of its seamless ability of wireless communication over internet. Raspberry Pi 3 has inbuilt Wi-Fi and Bluetooth, and Bluetooth is a very popular wireless communication Protocol. This guide covers two way text exchange between Raspberry pi and Android app BlueTerm over Bluetooth Interface

## Hardware Requirements:
- Raspberry Pi 2B or later
- USB Bluetooth adapter
- Android Smartphone
- Micro SD Card 16GB or higher
- Power bank

## Software Requirements:
- [Raspbian Jessie/Stretch](https://www.raspberrypi.org/downloads/raspbian/) running on `RPI` from SD card
- [BlueTerm application](https://play.google.com/store/apps/details?id=es.pymasde.blueterm) installed on Android phone

## Background:

Bluetooth programming in `Python` for data exchange and follows the socket programming model and communications between the Bluetooth devices is done through `RFCOMM` socket. RFCOMM (Radio Frequency Communication) is a Bluetooth Protocol which provided emulated RS-232 serial ports also known as Serial Port Emulation. Bluetooth serial port profile is based on this protocol. RFCOMM is very popular in Bluetooth applications because of its wide support and publically available API. It is bound to `L2CAP protocol`.

## Dependencies & Installation:

This guide assumes that you already have `Raspbian Jessie/Stretch` installed on SD card. Once you have a working Debian distribution set up next steps are covered in this guide. First you need to update Raspbian using below commands:

    $ sudo apt-get update
    $ sudo apt-get upgrade
    
Then we need to install few Bluetooth related packages followed by system reboot:

    $ sudo apt-get install bluetooth blueman bluez
    $ sudo reboot

`BlueZ` is an open source project and official Linux Bluetooth protocol stack. It supports all the core Bluetooth protocols and now become part of official Linux Kernel. `Blueman` provides the Desktop interface to manage and control the Bluetooth devices. Finally, we need python Library for Bluetooth communication so that we can send and receive data through `RFCOMM` using Python language:

    $ sudo apt-get install python-bluetooth

## Pairing Devices with Raspberry Pi over Bluetooth:

Next up is to pair Android phone with Raspberry pi. We have previously installed `BlueZ` package in RPi, which provides a command line utility called `bluetoothctl` to manage Bluetooth devices. Now invoke the `bluetoothctl` utility with below command:

    $ sudo bluetoothctl
You can check all the commands of bluetoothctl utility by typing `help`. To pair, we need to enter below commands in given order:

    [bluetooth]# power on
    [bluetooth]# agent on
    [bluetooth]# discoverable on
    [bluetooth]# pairable on
    [bluetooth]# scan on

After the last command `scan on`, you will see your Bluetooth device (Mobile phone) in the list. Make sure that your mobile has Bluetooth turned on and `visible` by nearby devices. Then copy the `MAC address` of you device and pair it with following command:

    $ pair <phone bluetooth address>

Then you will be prompted for Passcode or Pin in your Terminal console, type passcode there and press enter. Then type the same passcode in your mobile phone when prompted and you are now successfully paired with Raspberry Pi

## Android App BlueTerm:
Now after paring the Mobile Phone, we need to install Android App for communicating with Raspberry Pi using a Bluetooth Serial Adapter. As told earlier `RFCOMM` protocol emulates serial communication over `Bluetooth`, so we installed `BlueTerm` App which supports this protocol. 

You can also use any other Bluetooth Terminal App which supports communication via RFCOMM socket.
Now after downloading and installing the BlueTerm App, run Python script `BT_talk_dual.py` on RPI from the terminal and connect the paired raspberrypi device from the `BlueTerm` App at the same time.
After successful connection you will see `connected:raspberrypi` at the top right corner of the App. That’s it you can now have two way communication between RPI and Android phone, to terminate the server script running on RPI send `q` for quit from BlueTerm

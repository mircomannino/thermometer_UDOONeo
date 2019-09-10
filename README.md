# thermometer UDOONeo

What is needed is:
* 1 UDOO board
* 1 Servo motor 
* 1 MPL3115 sensor (barometer)

## How it works
When it is in function the sensor captures the external temperature and it's rappresented by a specific position of the servo hand.

First of all connect the sensor and the servo (digital pin: 9, there is the scheme in the image servo_scheme.png)  to the UDOO board.
> If your UDOO board is already on when you're connecting the MPL3115 sesor you should run the following commands to proceed:
> ``` 
> sudo rmmod mpl3115
>sudo modprobe mpl3115
> ```

> Otherwise, if you connect the sensor when the board is off you should not do anything, the boot process wiil do whatever it 
> takes.
> For any problem consult the official documentation (https://www.udoo.org/docs-neo/Hardware_&_Accessories/Bricks_snap_in_sensors.html)

**Only for 'thermometer.py' script** the next step is to run the following comand:
```
sudo ln -s /dev/ttyMCC /dev/ttyS0
```
It creates a soft link for the serial communication among the two processors of the UDOO board.

Once yuor setup is ready you can upload the arduino sketch on your UDOO board and run "termomther.sh" or "thermometer.py" from it.

## Temperature range
In this example the temperatures and angle degrees for the servo are descibed in the following tables

Temperatures  | Degree 
--------------|-------
25 | 150 
26 | 120 
27 | 90 
28 | 60
29 | 30

However if you want to increase the number of available temperatures (and its degree) you can modify the "map_temp" structure in the "thermometer.sh" or "thermometer.py" scripts.

## Debug 
The file "python_servo_control.py" is a simple python script that check if the servo receive the correct data.
With this script you can insert a position (in degrees) to send to the servo and it will take that position.


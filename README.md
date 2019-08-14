# thermometer_UDOONeo

What is needed is:
* 1 UDOO board
* 1 Servo motor 
* 1 MPL3115 sensor (barometer)

First of all connect the sensor and the servo (digital pin: 9)  to the UDOO board.
> If your UDOO board is already on when you're connecting the MPL3115 sesor you should run the following commands to proceed:
>  * sudo rmmod mpl3115
>  * sudo modprobe mpl3115

> Otherwise, if you connect the sensor when the board is off you should not do anything, the boot process wiil do whatever it 
> takes.
> For any problem consult the official documentation (https://www.udoo.org/docs-neo/Hardware_&_Accessories/Bricks_snap_in_sensors.html)

## Temperature range
In this example the temperatures and angle degrees for the servo are descibed in the following tables

Temperatures  | Degree 
--------------|-------
25 | 150 
26 | 120 
27 | 90 
28 | 60
29 | 30

However if you want to increase the number of available temperatures (and its degree) you can modify the "map_temp" structure in the "temp_to_servo.sh".

Once yuor setup is finished you can upload the arduino sketch on your UDOO board and run "temp_to_servo.sh" from it.


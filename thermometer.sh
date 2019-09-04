#!/bin/bash

# Bash script that reads the temperature from MPL3115 sensor end send it to 
# the servo motor.

# Creating the soft link if it doesn't exist
origin="/dev/ttyMCC"
newLink="/dev/ttyS0"
if [ ! -L "$newLink" ]; then 
    echo "Creating soft link: $newLink -> $origin"
    sudo ln -s $origin $newLink
    echo "Soft link created!"
fi

# Reading data from MPL3115
while [ 1 ]; do
    TEMP_RAW=`cat /sys/class/i2c-dev/i2c-1/device/1-0060/iio\:device0/in_temp_raw`
    TEMP_SCALE=`cat /sys/class/i2c-dev/i2c-1/device/1-0060/iio\:device0/in_temp_scale`
    python << EOF
import serial
import time
# mapping for temperatures
map_temp = {25: 150, 26: 120, 27: 90, 28: 60, 29: 30}
# Starting a serial communication
ser = serial.Serial("/dev/ttyS0", 115200, timeout=1)
ser.flushOutput()

temp = $TEMP_RAW * $TEMP_SCALE
degrees_to_servo = map_temp[int(temp)]
print("Temperature: " + str(int(temp)) + "* ")
print("Degrees servo: " + str(degrees_to_servo))
ser.write(chr(degrees_to_servo))
EOF

sleep 3
done

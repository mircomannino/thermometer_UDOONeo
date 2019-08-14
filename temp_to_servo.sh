#!/bin/bash

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
temp_to_servo = map_temp[int(temp)]
print("Temperatura: " + str(int(temp)) + "* ")
print(temp_to_servo)
ser.write(chr(temp_to_servo))
EOF

sleep 3
done

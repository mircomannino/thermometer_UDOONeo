import serial
import time

# Python script that reads the temperature from MPL3115 sensor end send it to
# the servo motor.

def main():
    # Reading data from the MPL3115 sensor
    TEMP_RAW = ""
    with open("/sys/class/i2c-dev/i2c-1/device/1-0060/iio\:device0/in_temp_raw", "r") as raw_file:
        TEMP_RAW = raw_file.read()
    TEMP_SCALE = ""
    with open("/sys/class/i2c-dev/i2c-1/device/1-0060/iio\:device0/in_temp_scale", "r") as scale_file:
        TEMP_SCALE = scale_file.read()

    # Open the serial communication
    ser = serial.Serial("/dev/ttyS0", 115200, timeout=1)
    ser.flushOutput()

    # mapping for temperatures
    map_temp = {25: 150, 26: 120, 27: 90, 28: 60, 29: 30}

    # Compute temperature and send it to the servo motor
    temp = int(TEMP_RAW) * int(TEMP_SCALE)
    temp_to_servo = map_temp[int(temp)]
    print("Temperatura: " + str(int(temp)) + "* ")
    print(temp_to_servo)
    ser.write(chr(temp_to_servo))

if __name__ == '__main__':
    main()

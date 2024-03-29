import serial
import time

# Python script that reads the temperature from MPL3115 sensor end send it to
# the servo motor.

def main():
    while(True):
        # Reading data from the MPL3115 sensor
        TEMP_RAW = ""
        with open("/sys/class/i2c-dev/i2c-1/device/1-0060/iio:device0/in_temp_raw", "r") as raw_file:
            TEMP_RAW = raw_file.read()
        TEMP_SCALE = ""
        with open("/sys/class/i2c-dev/i2c-1/device/1-0060/iio:device0/in_temp_scale", "r") as scale_file:
            TEMP_SCALE = scale_file.read()

        # Open the serial communication
        ser = serial.Serial("/dev/ttyS0", 115200, timeout=1)
        ser.flushOutput()

        # mapping for temperatures
        map_temp = {25: 150, 26: 120, 27: 90, 28: 60, 29: 30}

        # Compute temperature and send it to the servo motor
        temp = float(TEMP_RAW) * float(TEMP_SCALE)
        degrees_to_servo = map_temp[int(temp)]
        print("Temperatura: " + str(int(temp)) + "* ")
        print("Degrees servo: " + str(degrees_to_servo))
        ser.write(chr(degrees_to_servo))
    
        time.sleep(3)

if __name__ == '__main__':
    main()

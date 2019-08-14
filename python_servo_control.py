import serial
import time


ser = serial.Serial('/dev/ttyS0',115200,timeout=1)
ser.flushOutput()
#print 'Serial connected'

while(1):
	pos = input('Insert position(-1 to exit): ')
	if pos == -1:
		break
	else:
		ser.write(chr(pos))
		time.sleep(1)

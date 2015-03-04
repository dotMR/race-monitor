import serial
# import tweepy
import time
import os

ser = serial.Serial('/dev/tty.usbserial-A600e0BZ', 19200)
# serScroll = serial.Serial('/dev/tty.usbserial-A700fjv5', 9600)

path = 'out'
filename = 'results.txt'

if not os.path.exists(path):
    os.makedirs(path)

f = open(os.path.join(path, filename), 'a')
f.write("2015 Mario Cup Results")
f.write("\nFrom Docker\n")

# while True:
# 	data = ser.readline()

# 	if data.startswith('&'):
# 		data = data.replace('&', '')
# 		data = data.replace('!', '')
# 		data = data.replace('\r', '')
# 		data = data.replace('\n', '')
# 		obj = data.split('_')

# 		event = "E2"
# 		##course = obj[0]
# 		course = "C2"
# 		#course = "S2"

# 		racer = obj[1]
# 		racer_name = obj[2]
# 		time = obj[3]

# 		# scrollerOutput = str(racer_name) + ": " + str(time)
# 		fileOutput = str(racer_name) + " had a time of: " + str(time)
# 		f.write(fileOutput)
# 		# serScroll.write(scrollerOutput)

# ser.close()
f.close()
from sense_hat import SenseHat
import argparse

sense = SenseHat()
sense.clear()

parser = argparse.ArgumentParser(description="Small CLI to get sensor values out of the SenseHat.", epilog="Output format is a triple dash followed by the single character flag for the reading then the reading data is on the next line.")
parser.add_argument("-a", "--all", help="print all sensor data and exit", action="store_true")
parser.add_argument("-t", "--temperature", help="print temperature (celsius) readings to stdout", action="store_true")
parser.add_argument("-u", "--humidity", help="print humidity (percentage) readings to stdout", action="store_true")
parser.add_argument("-p", "--pressure", help="print pressure (millibars) readings to stdout", action="store_true")
parser.add_argument("-o", "--orientation", help="print orientation (pitch, yaw, roll) (degrees) readings to stdout", action="store_true")
# add joystick, display screen, calibration options?

args = parser.parse_args()

def printTemperature():
  print('---t')
  print(sense.temperature)

def printHumidity():
  print('---u')
  print(sense.humidity)

def printPressure():
  print('---p')
  print(sense.pressure)

def printOrientation():
  orientation = sense.get_orientation()
  print('---o')
  print(orientation.pitch)
  print(orientation.yaw)
  print(orientation.roll)

if (args.all):
  printTemperature()
  printHumidity()
  printPressure()
  printOrientation()
  exit(0)

if (args.temperature):
  printTemperature()

if (args.humidity):
  printHumidity()

if (args.pressure):
  printPressure()

if (args.orientation):
  printOrientation()

exit(0)

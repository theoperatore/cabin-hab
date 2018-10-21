import argparse;

parser = argparse.ArgumentParser(description="Small CLI to get sensor values out of the SenseHat");
parser.add_argument("-t", "--temperature", help="print temperature readings to stdout", action="store_true");
parser.add_argument("-u", "--humidity", help="print humidity readings to stdout", action="store_true");
parser.add_argument("-p", "--pressure", help="print pressure readings to stdout", action="store_true");
parser.add_argument("-o", "--orientation", help="print orientation readings to stdout", action="store_true");
# add joystick, display screen, calibration options?

args = parser.parse_args();

if (args.temperature):
  print("Output temperature:");

if (args.humidity):
  print("Output humidity:");

if (args.pressure):
  print("Output pressure:");

if (args.orientation):
  print("Output orientation:");

exit(0);

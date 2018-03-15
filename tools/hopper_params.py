


import odrive.core
import argparse
import sys


# Connect to device
print("Waiting for device...")
my_odrive = odrive.core.find_any('usb', [], printer=lambda x: None)
print("Connected!")

# Set some default parameters

motor1 = my_odrive.motor1
motor0 = my_odrive.motor0
pos1 = motor1.encoder.pll_pos
pos0 = motor0.encoder.pll_pos

# set integral gain to zero
motor1.vel_integrator_gain = 0
motor0.vel_integrator_gain = 0
print('motor1')

try:
  # If this assignment works, we are already in interactive mode.
  # so just drop out of script to existing shell
  interpreter = sys.ps1
except AttributeError:
  # We are not in interactive mode, so let's fire one up
  # Though let's be real, IPython is the way to go
  print('If you want to have an improved interactive console with pretty colors,')
  print('you can run this script in interactive mode with IPython with this command:')
  print('ipython -i explore_odrive.py')
  print('')
  # Enter interactive python shell with tab complete enabled
  import code
  import rlcompleter
  import readline
  readline.parse_and_bind("tab: complete")
  code.interact(local=locals(), banner='')

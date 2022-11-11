# System imports
import socket
import time
from time import sleep


# Local imports

#from ..hal import hal_dc_motor as dc_motor


from hal import hal_led as led
from hal import hal_input_switch as switch
import version as ver

def blink_led(delay):
    # Led Blink
    led.init()

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)


def main():
   switch.init()
   led.init()

   while(1):
       if(switch.read_slide_switch() == 1):
           led.set_output(0,1)
           sleep(0.2)
           led.set_output(0,0)
           sleep(0.2)
       else:
           #led.set_output(0,0)
           led.set_output(0, 1)
           sleep(0.1)
           led.set_output(0, 0)
           sleep(0.1)

# Main entry point
if __name__ == "__main__":
    main()
# These are instruction manuals for our program to use
from microbit import *
import music
from Motor_Control import *
from Message_Decoder import *

music.play(NYAN)

# How fast do we want the bus to go?
speed =
# What channel is our radio set to?
set_radio_channel( )        


# If the bus is on, keep reading this code over and over
while the_bus_is_on:
    # Open up the message from the controller and sorts the information
    instructions = open_message()
    
    # Look for the forward/backward information
    forward_backward_movement = instructions[are_we_going_forwards_or_backwards]
    # Look for the left/right information
    left_right_movement = instructions[are_we_going_left_or_right]

    # Tell the bus what you want it to do!
    move(forward_backward_movement, left_right_movement, speed)

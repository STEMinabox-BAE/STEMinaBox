# These are instruction manuals for our program to use
from microbit import *
from Bus_Control import *
from Message_Decoder import *

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
    # Have you remembered to indicate?
    left_indicator_on_off = instructions[is_the_left_indicator_on]
    right_indicator_on_off = instructions[is_the_right_indicator_on]
    # If it's dark, turn your lights on!
    lights_on_off = instructions[are_the_lights_on]
    # If you want to really annoy everyone, you'll need to use the horn!
    horn_on_off = instructions[is_the_horn_on]

    # Tell the bus what you want it to do!
    move(forward_backward_movement, left_right_movement, speed)
    indicators(left_indicator_on_off, right_indicator_on_off)
    lights(lights_on_off)
    horn(horn_on_off)

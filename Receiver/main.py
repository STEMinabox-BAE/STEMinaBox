from microbit import *
from Motor_Control import *
from Message_Decoder import *

speed = 
set_radio_channel( )



while the_bus_is_on:
    instructions = open_message()
    forward_backward_movement = instructions[are_we_going_forwards_or_backwards]
    left_right_movement = instructions[are_we_going_left_or_right]
    move(forward_backward_movement, left_right_movement, speed)

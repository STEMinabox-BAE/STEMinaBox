from microbit import *
from Motor_Control import *
from Message_Decoder import *

speed = 256
set_radio_channel(1)

while True:
    instructions = get_message()
    forward_backward = instructions[0]
    left_right = instructions[1]
    move(forward_backward, left_right, speed)

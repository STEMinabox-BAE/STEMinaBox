from microbit import *
from Motor_Control import *
from Message_Decoder import *

speed = 512
set_radio_channel(1)

f_b_instruction = 0
l_r_instruction = 1

while True:
    instructions = get_message()
    forward_backward = instructions[f_b_instruction]
    left_right = instructions[l_r_instruction]
    move(forward_backward, left_right, speed)
    sleep(10)

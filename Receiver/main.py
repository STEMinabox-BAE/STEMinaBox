from microbit import *
from Motor_Control import *
from Message_Decoder import *

motor_pins = [pin12, pin13, pin14, pin15]
speed = 256

while True:
    instructions = ['s', 's', 'q', 'd']
    instructions = get_message()
    forward_backward = instructions[f_b]
    left_right = instructions[l_r]
    move(forward_backward, left_right, speed)
    sleep(10)

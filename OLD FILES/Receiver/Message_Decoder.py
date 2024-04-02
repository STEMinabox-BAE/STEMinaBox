from microbit import *
import radio
import power

the_bus_is_on = True
are_we_going_forwards_or_backwards = 0
are_we_going_left_or_right = 1
are_the_lights_on = 2
is_the_horn_on = 3
is_the_left_indicator_on = 4
is_the_right_indicator_on = 5

radio.on()

keywords = ['(', '(', '(', 
            'f', 'b', 's', 
            ',', ',', ',',
            'r', 'l', 's', 
            ',', ',', ',',
            'l', 'd', 'd', 
            ',', ',', ',',
            'l', 'q', 'q', 
            ',', ',', ',',
            'l', 's', 's', 
            ',', ',', ',',
            'r', 's', 's',
            ')', ')', ')']

passive_message = list((keywords[5], keywords[11], keywords[17], keywords[23], keywords[29], keywords[35]))

# (s,s,d,q,l,s)

def set_radio_channel(desired_channel, desired_queue = 3, desired_power = 4):
    radio.config(queue = desired_queue, channel = desired_channel, power = desired_power)

def is_message_valid(message):
    for i in range(0, 13):
        if (message[i] != keywords[3*i]) and (message[i] != keywords[(3*i) + 1]) and (message[i] != keywords[(3*i) + 2]):
            return False
    return True

def open_message():
    message = radio.receive()
    if message != None:
        if message == 'STOP':
            power.off()
            return passive_message
        if is_message_valid(message):
            instructions = list((message[1], message[3], message[5], message[7], message[9], message[11]))
            return instructions
        return passive_message
    else:
        return passive_message

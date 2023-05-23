from microbit import *
import radio
import power

radio.on()

keywords = ['(', '(', '(', 'f', 'b', 's', ',', ',', ',',
            'r', 'l', 's', ')', ')', ')']

passive_message = list((keywords[5], keywords[11]))

def set_radio_channel(desired_channel, desired_queue = 10, desired_power = 4):
    radio.config(queue = desired_queue, channel = desired_channel, power = desired_power)

def is_message_valid(message):
    for i in range(0, 5):
        if (message[i] != keywords[3*i]) and (message[i] != keywords[(3*i) + 1]) and (message[i] != keywords[(3*i) + 2]):
            print('Invalid')
            return False
    return True

def get_message():
    message = radio.receive()
    if message != None:
        if message == 'STOP':
            power.off()
            return passive_message
        if is_message_valid(message):
            instructions = list((message[1], message[3]))
            return instructions
        return passive_message
    else:
        return passive_message
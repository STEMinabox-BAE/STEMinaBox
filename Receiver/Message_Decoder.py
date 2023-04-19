from microbit import *
import radio
import power

group_number = 1

radio.on()
radio.config(queue = 10, channel = group_number, power = 4)

keywords = ['(', '(', '(', 'f', 'b', 's', ',', ',', ',',
            'r', 'l', 's', ',', ',', ',', 'l', 'q', 'q',
            ',', ',', ',', 'l', 'd', 'd', ')', ')', ')']

passive_message = list((keywords[6], keywords[12], keywords[18], keywords[24]))

def is_message_valid(message):
    for i in range(0, 9):
        if (message[i] != keywords[3*i]) and (message[i] != keywords[(3*i) + 1]) and (message[i] != keywords[(3*i) + 2]):
            return False
    return True

def get_message():
    message = radio.receive()
    if message != None:
        if message == 'STOP':
            power.off()
            return passive_message
        if is_message_valid(message):
            instructions = list((message[1], message[3], message[5], message[7]))
            return instructions
        return passive_message
    else:
        return passive_message

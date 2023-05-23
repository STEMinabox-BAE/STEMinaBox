from microbit import *
import radio
radio.on()
radio.config(channel = 1)

# Forwards/Backwards
f = pin0
b = pin1
# Left/Right
l = pin9
r = pin8

check = True

message = ''

while True:
    incoming = radio.receive();
    old_message = message
    
    if incoming != 'stop': 
        if f.read_digital():
            message = '(f,'
        elif b.read_digital():
            message = '(b,'
        else:
            message = '(s,'
        if l.read_digital():
            message += 'l)'
        elif r.read_digital():
            message += 'r)'
        else:
           message += 's)'
    
    if incoming == 'stop':
        if not (f.read_digital() or b.read_digital() or l.read_digital() or r.read_digital()):
            incoming = None

    radio.send(message)



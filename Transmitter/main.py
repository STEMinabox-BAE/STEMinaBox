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

horn = pin2
lights = pin3
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
            message += 'l,'
        elif r.read_digital():
            message += 'r,'
        else:
           message += 's,'
        if horn.read_digital():
            message += 'l,'
        else:
            message += 'q,'
        if lights.read_digital():
            message += 'l)'
        else:
            message += 'd)'
    
    if incoming == 'stop':
        if not (f.read_digital() or b.read_digital() or l.read_digital() or r.read_digital()):
            incoming = None
            
    if message != old_message:
        radio.send(message)
        print(message)




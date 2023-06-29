from microbit import *
import radio
radio.on()
radio.config(channel = '''Each microbit will have a 
                    channel number on it, write it here''')

'''
Alernatively, this is the hardware version.
Simply attach a jumper between a 3V3 pin and 
one of the pins from the selection below:

pin11.set_pull(pin11.PULL_DOWN)
pin12.set_pull(pin12.PULL_DOWN)
pin13.set_pull(pin13.PULL_DOWN)
pin14.set_pull(pin14.PULL_DOWN)
pin15.set_pull(pin15.PULL_DOWN)
pin16.set_pull(pin16.PULL_DOWN)
pin19.set_pull(pin19.PULL_DOWN)
pin20.set_pull(pin20.PULL_DOWN)

if pin11.read_digital():
    radio.config(channel = 1)
if pin12.read_digital():
    radio.config(channel = 2)
if pin13.read_digital():
    radio.config(channel = 3)
if pin14.read_digital():
    radio.config(channel = 4)
if pin15.read_digital():
    radio.config(channel = 5)
if pin16.read_digital():
    radio.config(channel = 6)
if pin19.read_digital():
    radio.config(channel = 7)
if pin20.read_digital():
    radio.config(channel = 8)
'''

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
            display.show(Image.ARROW_N)
        elif b.read_digital():
            message = '(b,'
            display.show(Image.ARROW_S)
        else:
            message = '(s,'
        if l.read_digital():
            message += 'l)'
            display.show(Image.ARROW_W)
        elif r.read_digital():
            message += 'r)'
            display.show(Image.ARROW_E)
        else:
           message += 's)'
    
    if incoming == 'stop':
        if not (f.read_digital() or b.read_digital() or l.read_digital() or r.read_digital()):
            incoming = None

    radio.send(message)


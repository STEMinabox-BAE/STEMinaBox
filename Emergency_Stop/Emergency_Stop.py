from microbit import *
import radio

while True:
    if button_a.was_pressed() or button_b.was_pressed():
        radio.on()
        for i in range(84):
            for j in range(256):
                radio.config(channel = i, group = j, power = 7)
                for k in range(100):
                    radio.send('STOP')

from microbit import *
import radio

radio_channel = 23
radio_power = 7
radio.config(channel = radio_channel, power = radio_power)

while True:
    
    if button_a.is_pressed() and button_b.is_pressed():
        if button_a.get_presses()%10 == 0:
            radio.send("3")
    elif button_a.was_pressed:
        radio.send("1")
    elif button_b.was_pressed:
        radio.send("2")

    if pin_logo.is_touched():
        radio.send("4")

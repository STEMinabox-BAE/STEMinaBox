#CONTROLLER CODE
def on_button_pressed_a():
    radio.send_number(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    radio.send_number(3)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    radio.send_number(2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_touched():
    radio.send_number(4)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

radio.set_group(23)

#BUS CODE
def on_received_number(receivedNumber):
    global indicatorL, indicatorR, LEDstate
    if receivedNumber == 1:
        if indicatorL == 0:
            indicatorL = 1
        else:
            indicatorL = 0
    if receivedNumber == 2:
        if indicatorR == 0:
            indicatorR = 1
        else:
            indicatorR = 0
    if receivedNumber == 3:
        music.play(music.tone_playable(262, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
    if receivedNumber == 4:
        if LEDstate == 0:
            LEDstate = 1
        else:
            LEDstate = 0
radio.on_received_number(on_received_number)

indicatorR = 0
indicatorL = 0
LEDstate = 0
LEDstate = 0
indicatorL = 0
indicatorR = 0
radio.set_group(23)

def on_forever():
    if LEDstate == 1:
        pins.digital_write_pin(DigitalPin.P0, 1)
    else:
        pins.digital_write_pin(DigitalPin.P0, 0)
    while indicatorL == 1:
        pins.digital_write_pin(DigitalPin.P1, 0)
        basic.show_number(1)
        control.wait_micros(1000)
        pins.digital_write_pin(DigitalPin.P1, 1)
        basic.show_number(0)
        control.wait_micros(1000)
        break
    while indicatorR == 1:
        pins.digital_write_pin(DigitalPin.P2, 0)
        basic.show_number(6)
        control.wait_micros(1000)
        pins.digital_write_pin(DigitalPin.P2, 1)
        basic.show_number(9)
        control.wait_micros(1000)
        break
basic.forever(on_forever)


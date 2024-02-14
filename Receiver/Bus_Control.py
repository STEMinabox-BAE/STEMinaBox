from microbit import *
import music

# motor_pins = [pin12, pin13, pin14, pin15]
motor_pins = [pin8, pin12, pin0, pin16]
headlights = pin9
left_indicator = pin1
right_indicator = pin2

blink_wait = 0
output = False

'''Motor one is left side 
   Motor two is right side'''

# def move(_fb, _lr, speed):
#     m1_active = False
#     m1_speed = 0
#     m2_active = False
#     m2_speed = 0
#     if _fb = 'f':
#         m1_active = True
#         m1_speed = speed
#         m2_active = True
#         m2_speed = speed
#         if _lr == 'l':
#             m1_speed /= 2
#             m1_speed = int(m1_speed)
#         elif _lr == 'r':
#             m2_speed /= 2
#             m2_speed = int(m2_speed)

def indicators(_li, _ri):
    global blink_wait, output
    if blink_wait == 5000:
        output = not output
        if _li == 'l':
            left_indicator.write_digital(output)
        if _ri == 'r':
            right_indicator.write_digital(output)
        blink_wait = 0
    else:
        blink_wait = blink_wait + 1

def horn(_h):
    if _h == 'l':
        music.pitch(262, -1, pin13)
    elif _h == 'q':
        music.stop(pin13)

def lights(_hl):
    if _hl == 'l':
        headlights.write_digital(1)
    elif _hl == 'd':
        headlights.write_digital(0)

def move(_fb, _lr, _speed):
    op = 0
    on = 0
    tp = 0
    tn = 0
    if _fb == 'f':
        op = _speed
        tp = _speed
        if _lr == 'l':
            # tp += _speed
            op /= 2
            op = int(op)
        elif _lr == 'r':
            # op += _speed
            tp /= 2
            tp = int(tp)
    elif _fb == 'b':
        on = _speed
        tn = _speed
        if _lr == 'l':
            # tn += _speed
            on /= 2
            on = int(on)
        elif _lr == 'r':
            # on += _speed
            tn /= 2
            tn = int(tn)
    elif _fb == 's':
        if _lr == 'l':
            tp = _speed
        elif _lr == 'r':
            op = _speed
    if ((not (_fb == 's')) or (not (_lr == 's'))):
        print('bus changing dir')
        set_motors(op, on, tp, tn, motor_pins)

def set_motors(one_pos_val, one_neg_val, two_pos_val, two_neg_val, motor_pins):
    motor_pins[0].write_analog(one_pos_val)
    motor_pins[1].write_analog(one_neg_val)
    motor_pins[2].write_analog(two_pos_val)
    motor_pins[3].write_analog(two_neg_val)
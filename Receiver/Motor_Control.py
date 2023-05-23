from microbit import *

motor_pins = [pin12, pin13, pin14, pin15]

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
            op += _speed
        elif _lr == 'r':
            # op += _speed
            tp += _speed
    elif _fb == 'b':
        on = _speed
        tn = _speed
        if _lr == 'l':
            on += _speed
        elif _lr == 'r':
            tn += _speed
    elif _fb == 's':
        if _lr == 'l':
            tp = _speed
        elif _lr == 'r':
            op = _speed
    set_motors(op, on, tp, tn, motor_pins)

def set_motors(one_pos_val, one_neg_val, two_pos_val, two_neg_val, motor_pins):
    motor_pins[0].write_analog(one_pos_val)
    motor_pins[1].write_analog(one_neg_val)
    motor_pins[2].write_analog(two_pos_val)
    motor_pins[3].write_analog(two_neg_val)
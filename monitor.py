from time import sleep
import sys

def loop_for_print():
    for _ in range(6):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(1)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(1)

def is_out_of_range(value, minv, maxv):
    if minv != 'NA' and value < minv:
        return True
    if maxv != 'NA' and value > maxv:
        return True
    return False

def range_check(value, minv, maxv):
    if is_out_of_range(value, minv, maxv):
        loop_for_print()
        return False
    return True

def vitals_ok(temperature, pulseRate, spo2):
    checks = {
        "Temperature": range_check(temperature, 95, 102),
        "Pulse Rate": range_check(pulseRate, 20, 60),
        "SpO2": range_check(spo2, 90, 'NA')
    }

    for label, result in checks.items():
        if not result:
            print(f"{label} out of range")

    return all(checks.values())

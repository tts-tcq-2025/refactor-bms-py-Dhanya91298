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

def is_below_min(value, minv):
    return minv != 'NA' and value < minv

def is_above_max(value, maxv):
    return maxv != 'NA' and value > maxv

def is_out_of_range(value, minv, maxv):
    return is_below_min(value, minv) or is_above_max(value, maxv)

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

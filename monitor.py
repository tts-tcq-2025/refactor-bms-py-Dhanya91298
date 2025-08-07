
from time import sleep
import sys

def loop_for_print():
  for i in range(6):
    print('\r* ', end='')
    sys.stdout.flush()
    sleep(1)
    print('\r *', end='')
    sys.stdout.flush()
    sleep(1)
  
def range_check(value,minv,maxv):
    minv = None if minv == 'NA' else minv
    maxv = None if maxv == 'NA' else maxv

    if (minv is not None and value < minv) or (maxv is not None and value > maxv):
        loop_for_print()
        return False
    return True
  
def vitals_ok(temperature, pulseRate, spo2):
  rangeChecksMessages = {
        "Temperature ": range_check(temperature,95, 102),
        "pulseRate ": range_check(pulseRate, 20, 60),
        "spo2 ": range_check(spo2, 90, 'NA')
    }

  for label,checkResult in rangeChecksMessages.items():
        if not checkResult:
            print(label + "out of range")
    
  return all(rangeChecksMessages.values())


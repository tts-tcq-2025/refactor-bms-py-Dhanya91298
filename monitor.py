
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
  retVal = False
  if 'NA' not in minv or 'NA' not in maxv:
    if value > maxv or value < minv:
      loop_for_print()
    else:
       retVal = True
  else:
    if 'NA' in minv and value > maxv:
        loop_for_print()
    elif 'NA' in maxv and value<minv:
         loop_for_print()
    else:
       retVal = True
      
  return retVal
  
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


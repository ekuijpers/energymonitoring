#!/usr/bin/python
# Program to extract a value from the lm-sensors

import sys
import sensors

sensors.init()
sensorname = sys.argv[1]

try:
    for chip in sensors.iter_detected_chips():
        #      print '%s at %s' % (chip, chip.adapter_name)
        for feature in chip:
            if feature.label == sensorname:
                print '%s =%.2f ' % (feature.label, feature.get_value())
finally:
    sensors.cleanup()

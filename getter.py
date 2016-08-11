from emokit.emotiv import Emotiv
from datetime import datetime

import os, sys, time, errno, platform
# import matplotlib.pyplot as plt

if platform.system() == "Windows":
    import socket  # Needed to prevent gevent crashing on Windows. (surfly / gevent issue #459)
import gevent

idle_time       = 1
measure_time    = 2
sampling_rate   = 128

try :
    name    = sys.argv[1]
except:
    name    = 'unnamed'

try :
    maxtime = int(sys.argv[2])
except:
    maxtime = 10

if __name__ == "__main__":
    # headset = Emotiv(display_output=False)
    headset     = Emotiv()
    gevent.spawn(headset.setup)
    gevent.sleep(0)

    data        = {
        'second'    : [],
        'counter'   : [],
        'F3'        : [],
        'FC5'       : [],
        'AF3'       : [],
        'F7'        : [],
        'T7'        : [],
        'P7'        : [],
        'O1'        : [],
        'O2'        : [],
        'P8'        : [],
        'T8'        : [],
        'F8'        : [],
        'AF4'       : [],
        'FC6'       : [],
        'F4'        : []
    }
    # output.write("SECOND,COUNTER,F3,FC5,AF3,F7,T7,P7,O1,O2,P8,T8,F8,AF4,FC6,F4,GYRO_X,GYRO_Y\n")

    second      = 0
    iterate     = 0
    try:
        while ( true ):
            packet      = headset.dequeue()

            if (second % (measure_time + idle_time) >= measure_time ) :
                data['second'].append(time_now)
                data['counter'].append(packet.counter)
                data['F3'].append(packet.F3[0])
                data['FC5'].append(packet.FC5[0])
                data['AF3'].append(packet.AF3[0])
                data['F7'].append(packet.F7[0])
                data['T7'].append(packet.T7[0])
                data['P7'].append(packet.P7[0])
                data['O1'].append(packet.O1[0])
                data['O2'].append(packet.O2[0])
                data['P8'].append(packet.P8[0])
                data['T8'].append(packet.T8[0])
                data['F8'].append(packet.F8[0])
                data['AF4'].append(packet.AF4[0])
                data['FC6'].append(packet.FC6[0])
                data['F4'].append(packet.F4[0])
            elif (iterate == (sampling_rate - 1)) :
                print data

            iterate += 1
            if (iterate == sampling_rate) :
                iterate = 0
                second  += 1

            gevent.sleep(0)

    except KeyboardInterrupt:
        headset.close()
        os.system('clear')
    finally:
        headset.close()
        os.system('clear')

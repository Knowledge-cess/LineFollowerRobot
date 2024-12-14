from machine import Pin
from utime import sleep

# Proximity senson 
le = Pin(0, Pin.IN)
l = Pin(1, Pin.IN)
c = Pin(2, Pin.IN)
r = Pin(3, Pin.IN)
re = Pin(4, Pin.IN)

# Motor Left configuration
lIn1 = Pin(5, Pin.OUT)
lIn2 = Pin(6, Pin.OUT)
lIn1.value(1)
lIn2.value(1)

# Motor Right configuration
rIn1 = Pin(7, Pin.OUT)
rIn2 = Pin(8, Pin.OUT)
rIn1.value(1)
rIn2.value(1)

while True:
    if(c.value() == 0 and le.value() == 1 and l.value() == 1 and re.value() == 1 and r.value() == 1):
        lIn1.value(1)
        lIn2.value(0)
        rIn1.value(1)
        rIn2.value(0)

    elif(le.value() == 0 or l.value() == 0 ):
        lIn1.value(0)
        lIn2.value(1)
        rIn1.value(1)
        rIn2.value(0)
    
    elif(re.value() == 0 or r.value() == 0 ):
        lIn1.value(1)
        lIn2.value(0)
        rIn1.value(0)
        rIn2.value(1)
    
    else:
        lIn1.value(1)
        lIn2.value(1)
        rIn1.value(1)
        rIn2.value(1)

    print(le.value(),l.value(),c.value(),r.value(),re.value())
    # # # Motor 1
    # lIn1.value(0)
    # lIn2.value(1)
    # print('Running....',lIn1.value(),lIn2.value())
    # # Motor 2
    # rIn1.value(1)
    # rIn2.value(0)
    # sleep(0.5)
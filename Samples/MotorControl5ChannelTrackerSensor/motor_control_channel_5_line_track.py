from machine import Pin
from machine import PWM
from utime import sleep

# Proximity senson 
le = Pin(0, Pin.IN)
l = Pin(1, Pin.IN)
c = Pin(2, Pin.IN)
r = Pin(3, Pin.IN)
re = Pin(4, Pin.IN)

# Motor Left configuration

# Define PWM pins for speed control (EN1 and EN2)
en1 = PWM(Pin(14))  # Enable motor 1
lIn1 = Pin(5, Pin.OUT)
lIn2 = Pin(6, Pin.OUT)
lIn1.value(0)
lIn2.value(1)


# Motor Right configuration
en2 = PWM(Pin(15))  # Enable motor 2
rIn1 = Pin(7, Pin.OUT)
rIn2 = Pin(8, Pin.OUT)
rIn1.value(0)
rIn2.value(1)

en1.freq(50)
en2.freq(50)
speed = 20
en1.duty_u16(int(speed/100*65536))  # Set speed for motor 1
en2.duty_u16(int(speed/100*65536))  # Set speed for motor 2

while True:
   
    if(c.value() == 0 and le.value() == 1 and l.value() == 1 and re.value() == 1 and r.value() == 1):
        lIn1.value(1)
        lIn2.value(0)
        rIn1.value(1)
        rIn2.value(0)
        print("case 1")

    elif(le.value() == 0 or l.value() == 0 ):
        lIn1.value(0)
        lIn2.value(1)
        rIn1.value(1)
        rIn2.value(0)
        print("case 2")
    
    elif(re.value() == 0 or r.value() == 0 ):
        lIn1.value(1)
        lIn2.value(0)
        rIn1.value(0)
        rIn2.value(1)
        print("case 3")
    
    else:
        lIn1.value(1)
        lIn2.value(1)
        rIn1.value(1)
        rIn2.value(1)
        print("case 4")

    print('values ',le.value(),l.value(),c.value(),r.value(),re.value())
    # # # Motor 1
    # lIn1.value(0)
    # lIn2.value(1)
    # print('Running....',lIn1.value(),lIn2.value())
    # # Motor 2
    # rIn1.value(1)
    # rIn2.value(0)
    # sleep(0.5)
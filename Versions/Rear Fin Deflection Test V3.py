from machine import Pin, PWM
import utime

MIN = 100000
MID = 1400000
MAX = 1600000

pwm = PWM(Pin(14))
pwm.freq(50)

pwm1 = PWM(Pin(15))
pwm1.freq(50)

pwm2 = PWM(Pin(13))
pwm2.freq(50)

pwm3 = PWM(Pin(12))
pwm3.freq(50)

pwm4 = PWM(Pin(11))
pwm4.freq(50)


while True:
    utime.sleep(1)
    pwm.duty_ns(MAX)
    pwm1.duty_ns(MAX)
    pwm2.duty_ns(MAX)
    pwm3.duty_ns(MAX)
    pwm4.duty_ns(MAX)
    print("max")
    utime.sleep(1)
    pwm.duty_ns(MIN)
    pwm1.duty_ns(MIN)
    pwm2.duty_ns(MIN)
    pwm3.duty_ns(MIN)
    pwm4.duty_ns(MIN)
    print("min")
    utime.sleep(1)
    
    pwm.duty_ns(MID)
    pwm1.duty_ns(MID)
    pwm2.duty_ns(MID)
    pwm3.duty_ns(MID)
    pwm4.duty_ns(MID)
    print("mid")
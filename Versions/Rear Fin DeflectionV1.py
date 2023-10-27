from machine import Pin, PWM
import utime

#All code is written in MicroPython for the Raspberry Pi Pico

MIN = 450000
MID = 1000000
MAX = 1700000

pwm = PWM(Pin(16))
pwm.freq(50)

pwm1 = PWM(Pin(15))
pwm1.freq(50)

pwm2 = PWM(Pin(0))
pwm2.freq(50)

pwm3 = PWM(Pin(1))
pwm3.freq(50)


while True:
    utime.sleep(1)
    pwm.duty_ns(MAX)
    pwm1.duty_ns(MAX)
    pwm2.duty_ns(MAX)
    pwm3.duty_ns(MAX)
    print("max")
    utime.sleep(1)
    pwm.duty_ns(MIN)
    pwm1.duty_ns(MIN)
    pwm2.duty_ns(MIN)
    pwm3.duty_ns(MIN)
    print("min")
    utime.sleep(1)
    
    pwm.duty_ns(MID)
    pwm1.duty_ns(MID)
    pwm2.duty_ns(MID)
    pwm3.duty_ns(MID)
    print("mid")

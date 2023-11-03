from imu import MPU6050 
import time
from machine import Pin, I2C

from machine import Pin, PWM
import utime

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
imu = MPU6050(i2c)

#Front Fin Section
MIN = 600000
MID = 900000
MAX = 1200000

pwm = PWM(Pin(14))
pwm.freq(50)

pwm1 = PWM(Pin(15))
pwm1.freq(50)

#Rear Fin Section
MIN1 = 700000
MID1 = 900000  
MAX1 = 1200000
 

#Rear3#
pwm2 = PWM(Pin(13))
pwm2.freq(50)

#Rear2#
pwm3 = PWM(Pin(12))
pwm3.freq(50)

#Rear1#
pwm4 = PWM(Pin(11))
pwm4.freq(50)



while True:
    
    # Temperature display
    print("Temperature: ", round(imu.temperature,2), "°C")

    # reading values
    acceleration = imu.accel
    gyroscope = imu.gyro 
        
            
    if gyroscope.y > 45:
        print("Rotation backward") 
        pwm.duty_ns(MAX)
        pwm1.duty_ns(MIN)
        
    if gyroscope.y < -45:
        print("Rotation forward")
        pwm.duty_ns(MIN)
        pwm1.duty_ns(MAX)
        
        
    if gyroscope.z > 45:
        print("Twist left")
        pwm2.duty_ns(MIN1)
        pwm3.duty_ns(MIN1)
        pwm4.duty_ns(MIN1)
        
        
    if gyroscope.z < -45:
        print("Twist right")
        pwm2.duty_ns(MAX1)
        pwm3.duty_ns(MAX1)
        pwm4.duty_ns(MAX1)
    
    
    
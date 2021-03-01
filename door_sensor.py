#Import the libraries
import RPi.GPIO as GPIO
import time

#Set GPIO mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)

#Set GPIO pins
GPIO_TRIGGER = 7
GPIO_ECHO = 11

#Set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    #set trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
    
    #set trigger after0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    startTime = time.time()
    stopTime = time.time()

    #save start time
    while GPIO.input(GPIO_ECHO) == 0:
        startTime = time.time()
    
    while GPIO.input(GPIO_ECHO) == 1:
        stopTime = time.time()
    
    #calculate time
    timeElapsed = stopTime - startTime

    #multiply by the sonic speed (34300 cm/s)
    #and divide by 2, because there and back
    distance = (timeElapsed * 34300) / 2

    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print("Measured Distance =%.1f cm" % dist)
            time.sleep(1)
    #reset by pressint CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
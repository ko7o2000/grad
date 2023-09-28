import RPi.GPIO as GPIO

servoPin        = 12
DUTY_MAX  = 12    #DEGREE = 180
DUTY_MIN  = 3     #DEGREE = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPin, GPIO.OUT)

servo = GPIO.PWM(servoPin, 50)
servo.start(0)


def setServoDuty(degree):
    if degree > 180:
        degree = 180

    if degree < 0:
        degree = 0

    duty = DUTY_MIN + (degree * (DUTY_MAX - DUTY_MIN)/180.0)

    print("[Degree: %d] to [Duty : %0.2f]"%(degree, duty))
    
    servo.ChangeDutyCycle(duty)


import math

sound_volume = 100.0
user_x = 0.0
user_y = 0.0
distance = 25.0
distance_temp = 0.0
angle = 0.0
angle_temp = 0.0

while True:
    print("x 좌표 : ")
    user_x = float(input())
    print("y 좌표 : ")
    user_y = float(input())
    
    distance_temp = math.sqrt(user_x*user_x + user_y*user_y)
    sound_volume = 100.0 * distance_temp / distance

    angle_temp = math.atan(user_y/user_x) * 180.0 / math.pi

    print("Sound Volume : %0.2f\nChange of Angle : %0.2f" % (sound_volume, angle_temp - angle))
    print("=============================================")

    angle = angle_temp
    distance = distance_temp
    

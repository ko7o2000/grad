import pygame
import math
import numpy as np

standard_rssi = -35.0
rssi = [0.0, 0.0, 0.0]
x_beacon = [6.6, 2.8, -1.0]
y_beacon = [5.2, 0.2, -8.0]
distance = [0.0, 0.0, 0.0]
sound_volume = 1.0
sound_volume_temp = 1.0
angle = 0.0
angle_temp = 0.0

pygame.mixer.init()
p = pygame.mixer.Sound('promised_land.mp3')
p.play(-1)

distance_max = math.pow(10, (standard_rssi + 100.0)/(10*4) )
distance_speaker = distance_max


while True:
    for i in range(3):
        print("%d번째 RSSI : " %(i+1))
        rssi[i] = float(input())

    for i in range(3):
        distance[i] = math.pow(10, (standard_rssi - rssi[i])/(10*2) )

    a_matrix = np.array(
        [
            [x_beacon[0]-x_beacon[1], y_beacon[0]-y_beacon[1]],
            [x_beacon[0]-x_beacon[2], y_beacon[0]-y_beacon[2]]
        ]
    )
    b_matrix = np.array(
        [
            [0.5 * (distance[1]*distance[1]-distance[0]*distance[0] + x_beacon[0]*x_beacon[0]-x_beacon[1]*x_beacon[1] + y_beacon[0]*y_beacon[0]-y_beacon[1]*y_beacon[1])],
            [0.5 * (distance[2]*distance[2]-distance[0]*distance[0] + x_beacon[0]*x_beacon[0]-x_beacon[2]*x_beacon[2] + y_beacon[0]*y_beacon[0]-y_beacon[2]*y_beacon[2])]
        ]
    )

    x_matrix = np.linalg.lstsq(a_matrix, b_matrix, rcond= -1)
    user_x = x_matrix[0][0, 0]
    user_y = x_matrix[0][1, 0]

    print("d1 : %0.2f, d2 : %0.2f, d3 : %0.2f"%(distance[0], distance[1], distance[2]))
    print("x : %0.2f, y : %0.2f"%(user_x, user_y))

    distance_temp = math.sqrt(user_x*user_x + user_y*user_y)
    if distance_temp>distance_max:
        distance_temp = distance_max
    sound_volume = sound_volume_temp * distance_temp / distance_speaker

    angle_temp = math.atan(user_y/user_x) * 180.0 / math.pi

    print("Sound Volume : %0.2f\nChange of Angle : %0.2f" % (sound_volume, angle_temp - angle))
    print("=============================================")

    p.set_volume(sound_volume)
    
    angle = angle_temp
    distance_speaker = distance_temp
    sound_volume_temp = sound_volume

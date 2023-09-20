import math
import numpy as np

standard_rssi = -35.0
rssi = [0.0, 0.0, 0.0]
x_beacon = [6.6, 2.8, -1.0]
y_beacon = [5.2, 0.2, -8.0]
distance = [0.0, 0.0, 0.0]
x_user = 0.0
y_user = 0.0

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
x_user = x_matrix[0][0, 0]
y_user = x_matrix[0][1, 0]

print("%0.2f %0.2f %0.2f"%(distance[0], distance[1], distance[2]))
print(x_user)
print(y_user)

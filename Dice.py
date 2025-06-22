from sense_hat import SenseHat
from random import randint
from time import sleep
sense = SenseHat()
E = [0, 0, 0]
W = [255, 255, 255]
R = [255, 0, 0]
G = [0, 255, 0]
O = [255, 165, 0]
B = [0, 0, 255]
Y = [255, 255, 0]

hungary = [E, E, E, E, E, E, E, E,
           R, R, R, R, R, R, R, R,
           R, R, R, R, R, R, R, R,
           W, W, W, W, W, W, W, W,
           W, W, W, W, W, W, W, W,
           G, G, G, G, G, G, G, G,
           G, G, G, G, G, G, G, G,
           E, E, E, E, E, E, E, E]

ireland = [E, G, G, W, W, O, O, E,
           E, G, G, W, W, O, O, E,
           E, G, G, W, W, O, O, E,
           E, G, G, W, W, O, O, E,
           E, G, G, W, W, O, O, E,
           E, G, G, W, W, O, O, E,
           E, G, G, W, W, O, O, E,
           E, G, G, W, W, O, O, E]

france = [E, B, B, W, W, R, R, E,
          E, B, B, W, W, R, R, E,
          E, B, B, W, W, R, R, E,
          E, B, B, W, W, R, R, E,
          E, B, B, W, W, R, R, E,
          E, B, B, W, W, R, R, E,
          E, B, B, W, W, R, R, E,
          E, B, B, W, W, R, R, E]

poland = [E, E, E, E, E, E, E, E,
          W, W, W, W, W, W, W, W,
          W, W, W, W, W, W, W, W,
          W, W, W, W, W, W, W, W,
          R, R, R, R, R, R, R, R,
          R, R, R, R, R, R, R, R,
          R, R, R, R, R, R, R, R,
          E, E, E, E, E, E, E, E]
          
austria = [E, E, E, E, E, E, E, E,
           R, R, R, R, R, R, R, R,
           R, R, R, R, R, R, R, R,
           W, W, W, W, W, W, W, W,
           W, W, W, W, W, W, W, W,
           R, R, R, R, R, R, R, R,
           R, R, R, R, R, R, R, R,
           E, E, E, E, E, E, E, E]

finland = [E, E, E, E, E, E, E, E,
           W, W, B, B, W, W, W, W,
           W, W, B, B, W, W, W, W,
           B, B, B, B, B, B, B, B,
           B, B, B, B, B, B, B, B,
           W, W, B, B, W, W, W, W,
           W, W, B, B, W, W, W, W,
           E, E, E, E, E, E, E, E]

bonus = [E, E, E, E, E, E, E, E,
         E, W, W, E, E, W, W, E,
         E, W, B, E, E, W, B, E,
         E, E, E, E, E, E, E, E,
         E, E, E, E, E, E, E, E,
         Y, E, E, E, E, E, E, Y,
         E, Y, Y, Y, Y, Y, Y, E,
         E, E, E, E, E, E, E, E]

oldnum = 0

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    
    x = abs(x)
    y = abs(y)
    z = abs(z)
    
    if x > 1.2 or y > 1.2 or z > 1.2:
        num = randint (1, 6)
        print (num)
        if num == 1:
            sense.set_pixels(hungary)
        if num == 2:
            sense.set_pixels(ireland)
        if num == 3:
            sense.set_pixels(france)
        if num == 4:
            sense.set_pixels(poland)
        if num == 5:
            sense.set_pixels(austria)
        if num == 6:
            sense.set_pixels(finland)
        if oldnum == num:
            sense.set_pixels(bonus)
            sleep(2)
            print ("bonus")
        oldnum = num
        sleep(1)
    else:
        sense.clear()
    


from sense_hat import SenseHat
import time
import random

sense = SenseHat()
sense.clear()

delay = 0.8

#declare color tuples
r = (255,0,0)
b = (0,255,255)
p = (128,0,128)
g = (0, 255, 0)
w = (255,255,255)
k = (0,0,0)

all_arrows =[   
w,p,r,w,w,b,b,b,
p,p,r,r,g,w,b,w,
w,p,r,g,g,g,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w
]

no_arrow = [
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w
]

left_arrow =[   
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,p,w,w,w,w,w,w,
p,p,w,w,w,w,w,w,
w,p,w,w,w,w,w,w
]

right_arrow =[   
w,w,r,w,w,w,w,w,
w,w,r,r,w,w,w,w,
w,w,r,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w
]

down_arrow =[   
w,w,w,w,w,b,b,b,
w,w,w,w,w,w,b,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w
]

up_arrow =[   
w,w,w,w,w,w,w,w,
w,w,w,w,g,w,w,w,
w,w,w,g,g,g,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w
]

def move_left():
  sense.set_pixels(0, 1, p)
  time.sleep(delay)
  


sense.set_pixels(all_arrows)

from sense_hat import SenseHat
import time
import random

sense = SenseHat()
sense.clear()

speed = 0.8

#declare color tuples
r = (255,0,0)
b = (0,255,255)
p = (128,0,128)
g = (0, 255, 0)
w = (255,255,255)
k = (0,0,0)

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
w,p,w,w,w,w,w,w,
p,p,w,w,w,w,w,w,
w,p,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w
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



while True:
  sense.set_pixels(left_arrow)
  time.sleep(0.01)
  sense.set_pixels(right_arrow)
  time.sleep(0.01)
  sense.set_pixels(up_arrow)
  time.sleep(0.01)
  sense.set_pixels(down_arrow)
  time.sleep(0.01)

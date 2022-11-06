from PIL import Image
from math import *

im = Image.open('flower.jpg') # Can be many different formats.
pix = im.load()

IMG_WIDTH = im.size[0]
IMG_HEIGHT = im.size[1]

'''
OUT_WIDTH = 80
OUT_HEIGHT = 80

INC = max(ceil(IMG_WIDTH/OUT_WIDTH), ceil(IMG_HEIGHT/OUT_HEIGHT))
'''

INC = 4

arr = [[0 for i in range(IMG_WIDTH//INC)] for j in range(IMG_HEIGHT//INC)]


print("Image Dimensions:", IMG_WIDTH, IMG_HEIGHT, \
    "Output Dimensions:", IMG_WIDTH//INC, IMG_HEIGHT//INC, \
    "Reduced by:", INC)


for i in range(im.size[0]//INC) : 
    for j in range(im.size[1]//INC) :

        r = 0
        g = 0
        b = 0

        for p in range(INC) :
            for q in range(INC) :
                r += pix[i*INC+p, j*INC+q][0]
                g += pix[i*INC+p, j*INC+q][1]
                b += pix[i*INC+p, j*INC+q][2]
                
    
        r //= INC*INC
        g //= INC*INC
        b //= INC*INC

        if (r+g+b) < 600 :
            r = 0
            g = 0
            b = 0
            arr[j][i] = 1

        else :
            r = 255
            g = 255
            b = 255
        

        for p in range(INC) :
            for q in range(INC) :
                pix[i*INC+p, j*INC+q] = (r, g, b)
    

im.save('flower2.jpg')


'''
[1] = pen down
[2] = pen up
[3, x] = x right
[4] = down one and move to left end
'''
insts = []


pen_down = 0
pen_count = 0

for i in range(IMG_HEIGHT//INC) :
    for j in range(IMG_WIDTH//INC) :

        if(not pen_down) :
            if(arr[i][j]) :
                insts.append([3, pen_count])

                pen_down = 1
                pen_count = 1
            
            else :
                pen_count += 1 #0 steps
            
        else :
            if(arr[i][j]) :
                pen_count += 1 #1 steps

            else :
                insts.append([1])
                insts.append([3, pen_count])
                insts.append([2])

                pen_down = 0
                pen_count = 1
        
        
        if(arr[i][j]) :
            print("*", end="")
        else :
            print(" ", end="")
    print()

    if(pen_down) :
        insts.append([1])
        insts.append([3, pen_count])
        insts.append([2])

    pen_count = 0
    pen_down = 0
    insts.append([4])



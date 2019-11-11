import os

from fpdf import FPDF
from PIL import Image
from PIL import ImageDraw 

#width and height of image (1:2 ratio), height is limiting 
ih = 2000
iw =  1000

#draw crop/trim lines for cutting
def drawlines(ImageDraw):
    for i in range(0,6):
        for k in range(0,3):
            ImageDraw.line((i*iw+25,ih*k-35+25,i*iw+25,ih*k+35+25),fill="#707070",width =3)
            ImageDraw.line((i*iw-35+25,k*ih+25,i*iw+35+25,k*ih+25),fill="#707070",width =3)

#coordinates of image
x,y = 25,25

directory = 'tickets'
tile = Image.new('RGB', (5050,4050), color="white")
i = 0
#loop througtile = Image.new('RGB', (round(4000*11/8.5),4000), color="white")h all images
for filename in os.listdir(directory):
    if filename.endswith('.png'):
        im = Image.open(directory+'/'+filename)
        if x<=iw*4+25 and y<=ih+25:
            tile.paste(im,(x,y))
            x+=iw #move to next column
        #check if page has been filled
        if x==iw*5+25 and y==ih+25:
            #draw guidelines
            tile_draw = ImageDraw.Draw(tile)
            drawlines(tile_draw)
            #save image
            tile.save('tiles/'+str(i)+'_3.png')
            #next image
            x,y = 25,25
            i+=1
            tile = Image.new('RGB', (5175,4000), color="white")
        elif x == iw*5+25: #check if row has been filled
            y=ih+25 #move y to next row
            x=25
        print('tiles/'+str(i)+'.png')   
# tile_draw = ImageDraw.Draw(tile) 
# drawlines(tile_draw)
# tile.save('tiles/'+str(i)+'.png')

print('all done!')
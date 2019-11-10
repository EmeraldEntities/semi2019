import os

from fpdf import FPDF

#create pdf
pdf=FPDF('L','pt','letter')
pdf.add_page()
pdf.set_compression(True)

#width and height of image (1:2 ratio), height is limiting 
ih = pdf.h
iw = ih*11/8.5000000

#coordinates of image
x,y = 0,0

directory = 'tile'
#loop through all images
for i in range(0,32):
    pdf.image(directory+'/'+str(i)+'_1.png',0,0,'png')
    pdf.add_page()
    # print(filename)    
    print(i)

pdf.output(directory+'/'+'ticket-tiled-2.pdf', 'F')

print('all done!')
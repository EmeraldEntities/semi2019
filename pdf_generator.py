import os

from fpdf import FPDF
from PIL import Image

#draw crop/trim lines for cutting
def drawlines(FPDF):
    #image dimensions
    ih = FPDF.h/2.00000
    iw =  ih/2.0000
    for i in range(6):
        FPDF.line(i*iw-5,ih,i*iw+5,ih)
        if i!=0:
            for k in range(3):
                FPDF.line(i*iw,ih*k-5,i*iw,ih*k+5)

#create pdf
pdf=FPDF('L','pt','letter')
pdf.add_page()

#width and height of image (1:2 ratio), height is limiting 
ih = pdf.h/2.00000
iw =  ih/2.0000

#coordinates of image
x,y = 0,0

directory = 'tickets-test'
#loop through all images
for filename in os.listdir(directory):
    if x<=iw*4 and y<=ih:
        pdf.image(directory + '/'+filename,x,y,iw,ih,'png')
        x+=iw #move to next column
    #check if page has been filled
    if x==iw*5 and y==ih:
        drawlines(pdf)
        pdf.add_page()
        x,y=0,0
    elif x == iw*5: #check if row has been filled
        y=ih #move y to next row
        x=0
    print(filename)    
drawlines(pdf)

pdf.output(directory+'/'+'ticket.pdf', 'F')

print('all done!')
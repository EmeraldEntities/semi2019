# importing necessary libraries 
import img2pdf 
import os 
import argparse

#set layout
letter = (img2pdf.in_to_pt(11), img2pdf.in_to_pt(8.5))
layout = img2pdf.get_layout_fun(letter)

directory = 'tiles'
images = []
for i in range(0, 31 + 1):
    filename = directory+'/'+str(i)+'.png'
    images.append(filename)

with open('tiles/tickets.pdf', "wb") as out:
    out.write(img2pdf.convert(images,layout_fun=layout))

# output 
print("all done!") 

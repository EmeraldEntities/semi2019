# importing necessary libraries 
import img2pdf 
import os 
import argparse

#set layout
letter = (img2pdf.in_to_pt(11), img2pdf.in_to_pt(8.5))
layout = img2pdf.get_layout_fun(letter)

# with open('tile/test.pdf', "wb") as out_file:
#     images = []
#     for i in range(0, 31 + 1):
#         fname = str(i) + '_1.png'
#         images.append(fname)
#         print(fname)
#     out_file.write(img2pdf.convert(images))

def process_images(min_range, max_range, prefix, suffix, out_file,layout):
    images = []
    for i in range(min_range, max_range + 1):
        fname = prefix + str(i) + suffix
        images.append(fname)
    out_file.write(img2pdf.convert(images,layout_fun=layout))

with open('tile/img2pdf-2-2.pdf', "wb") as out_file:
    process_images(0, 31, 'tile/', '_2.png', out_file,layout)

# directory = 'tile/'

# images=[]
# # images.append(None)
# for filename in os.listdir(directory):
#     if filename.endswith('png'):
#         images.append(Image.open(directory+filename))

# # with open('tile/test.pdf', 'wb') as f:
# #     f.write(img2pdf.convert(images, layout_fun=layout))
# #     print(filename)

# images[0].save('tile/test.pdf', save_all = True, quality=100, append_images = images[1:])

# closing pdf file 

# output 
print("Successfully made pdf file") 

"#-*- coding:utf-8 -*-"
from PIL import Image
import argparse


parse = argparse.ArgumentParser()
parse.add_argument('file')  
parse.add_argument('-o','--output')
parse.add_argument('--width',type = int,default = 80)
parse.add_argument('--height',type = int,default = 80)


args = parse.parse_args()
IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r,g,b,alpha = 256):
	if alpha == 0:
		return ' '
	length = len(ascii_char)
	gray = int(0.2126*r + 0.7152*g + 0.0722*b)

	unit = (256.0 + 1)/length
	return ascii_char[int(gray/unit)]

if __name__ == '__main__':

	im = Image.open(IMG)
	im = im.resize((WIDTH,HEIGHT),Image.NEAREST)

	text = ""

	for i in range(HEIGHT):
		for j in range(WIDTH):
			tet += get_char(*im.getpixl((j,i)))
		txt += '\n'
	print txt



	if OUTPUT:
		with open(OUTPUT,'w') as f:
			f.write (txt)
			
	else:
		with  open ("output.txt","w") as f:
			f.write(txt)




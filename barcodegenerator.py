# pip install python_barcode
from barcode.ean import EAN13
from typing import Text
import barcode
from barcode import writer

from barcode.writer import ImageWriter
string = " Welcome to Python Programming Language "

text = str(string)


code = barcode.get_barcode_class("code128")

image = code(string, writer=ImageWriter())

save_img = image.save('My final Barcode')

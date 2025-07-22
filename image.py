import escpos
from PIL import Image

ALLOWED_TYPES = ['bitImageRaster', 'bitImageColumn']
PRINTER_WIDTH = 576

def print_image(printer: escpos.escpos.Escpos, image_path: str, convert = True,  impl: str = 'bitImageRaster', preview: bool = False, print = True):

    img = Image.open(image_path)

    if convert:
        w_percent = PRINTER_WIDTH/ float(img.size[0])
        h_size = int((float(img.size[1]) * float(w_percent)))
        img = img.resize((PRINTER_WIDTH, h_size))
        img = img.convert("L")

    if preview:
        img.show()

    if print:
        printer.image(img, impl=impl)


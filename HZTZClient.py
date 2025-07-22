from escpos.printer import Usb
from PIL import Image

from heb import CODE_EIGHT

ALLOWED_TYPES = ['bitImageRaster', 'bitImageColumn']
PRINTER_WIDTH = 576


class HZTZClient(Usb):
    """
    HZTZClient is a subclass of escpos.printer.Usb that provides additional functionality
    for printing Hebrew text with specific code pages and alignment options.
    """
    def __init__(self, printer:Usb, **kwargs):
        super().__init__(usb_args=printer.usb_args)
        self._printer = printer

    @classmethod
    def from_escpos(cls, escpos_printer: Usb, **kwargs):
        """
        Initialize the HZTZClient with an existing escpos printer instance.
        """
        return cls(escpos_printer, **kwargs)


    def print_hebrew_text(self, text: str, code_page: bytes = CODE_EIGHT, align_right: bool = True, padding: int = 0):
        self._printer._raw(code_page)

        hebrew_reversed = text[::-1]
        encoded = hebrew_reversed.encode('cp862')


        if align_right:
            self._printer.set(align='right')
        self._printer._raw(encoded)

        if padding > 0:
            self._printer.print_and_feed(padding)
        self._printer.set(align='left')  # Reset alignment to left after printing

    def print_image(self, image_path: str, convert = True,  impl: str = 'bitImageRaster', preview: bool = False, print = True):
        img = Image.open(image_path)

        if convert:
            w_percent = PRINTER_WIDTH/ float(img.size[0])
            h_size = int((float(img.size[1]) * float(w_percent)))
            img = img.resize((PRINTER_WIDTH, h_size))
            img = img.convert("L")

        if preview:
            img.show()

        if print:
            self._printer.image(img, impl=impl)



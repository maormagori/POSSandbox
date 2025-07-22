import escpos.escpos

from HZTZClient import HZTZClient
from printer import get_printer


def example_receipt(p: escpos.escpos.Escpos):
    # Store name in bold and center
    p.set(align="center", bold=True, width=2, height=2)
    p.text("My Store Name\n")

    p.set(align="center", bold=False)
    p.text("123 Main Street\n")
    p.text("City, Country\n")
    p.text("Tel: 123-456789\n")
    p.text("--------------------------------\n")

    # Items
    p.set(align="center", bold=True)
    p.text("{:<20}{:>10}\n".format("Item", "Price"))
    p.text("--------------------------------\n")

    p.set(bold=False)
    p.text("{:<20}{:>10}\n".format("Apple", "$1.00"))
    p.text("{:<20}{:>10}\n".format("Banana", "$0.50"))
    p.text("{:<20}{:>10}\n".format("Orange", "$0.80"))

    p.text("--------------------------------\n")
    p.set(bold=True)
    p.text("{:<20}{:>10}\n".format("Total", "$2.30"))
    p.text("--------------------------------\n")

    # Thank you message
    p.set(align="center")
    p.text("\nThank you for shopping!\n")
    p.text("Visit us again!\n\n")

    # Cut the paper
    p.cut()


def main():
    printer: escpos.printer.Usb = get_printer()

    hztz_client = HZTZClient(printer)


if __name__ == "__main__":
   main()
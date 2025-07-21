from escpos import config

def get_printer():
    printer_config = config.Config()
    printer_config.load('./config.yaml')

    return printer_config.printer()

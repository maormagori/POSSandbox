from escpos import config

from pathlib import Path

PROJECT_DIR = Path(__file__).parent
CONFIG_FILE = PROJECT_DIR / 'config.yaml'


def get_printer():
    printer_config = config.Config()

    if not CONFIG_FILE.exists():
        raise FileNotFoundError(f"Configuration file not found: {CONFIG_FILE}")


    printer_config.load(str(CONFIG_FILE))

    return printer_config.printer()
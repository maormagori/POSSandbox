import escpos

# code page 8 (Hebrew) - slightly slim
CODE_EIGHT = b'\x1b\x74\x08'

# code page 62 (Hebrew) - slightly bold
CODE_SIXTY_TWO = b'\x1b\x74\x3e'

def print_hebrew_text(p: escpos.escpos.Escpos, text: str, code_page: bytes = CODE_EIGHT, align_right: bool = True, padding: int = 0):
    """Print Hebrew text with specified code page and alignment."""
    p._raw(code_page)

    hebrew_reversed = text[::-1]
    encoded = hebrew_reversed.encode('cp862')


    if align_right:
        p.set(align='right')
    p._raw(encoded)

    if padding > 0:
        p.print_and_feed(padding)
    p.set(align='left')  # Reset alignment to left after printing


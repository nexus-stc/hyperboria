def is_pdf(f):
    return len(f) > 4 and f[:4] == b'%PDF'

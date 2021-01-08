from pdfminer.high_level import extract_text


def is_pdf(path_to_file):
    try:
        extract_text(path_to_file, maxpages=1)
        return True
    except Exception:
        return False

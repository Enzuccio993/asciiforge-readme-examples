"""Turn Latin-script text into a simple ASCII URL slug."""
import re
import unicodedata


def slugify(title):
    normalized = unicodedata.normalize('NFKD', title)
    ascii_text = normalized.encode('ascii', errors='ignore').decode('ascii')
    return re.sub(r'[^a-z0-9]+', '-', ascii_text.lower()).strip('-')

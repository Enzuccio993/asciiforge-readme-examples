"""Count logical lines, including a final line without a newline."""
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', type=Path, help='UTF-8 text file')
    args = parser.parse_args()
    try:
        lines = args.file.read_text(encoding='utf-8').splitlines()
    except (OSError, UnicodeError) as error:
        parser.exit(1, 'Cannot read the UTF-8 file: ' + str(error) + '\n')
    print(str(len(lines)) + ' lines')


if __name__ == '__main__':
    main()

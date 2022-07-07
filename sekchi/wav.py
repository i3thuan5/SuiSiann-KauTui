from pathlib import Path
import sys
import re


def mikilim_to_wav(path):
    for file in Path(path).glob('**/*'):
        matched = re.match(r'[Pp]art([0-9])-\(([0-9]{1,4})\)\.wav', file.name)
        if not matched:
            print(file.name)
            continue
        print(file.name)
        print(matched.group(1, 2))


if __name__ == '__main__':
    path = sys.argv[1]
    mikilim_to_wav(path)

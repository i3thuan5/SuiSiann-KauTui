from pathlib import Path
import sys
import re


def element_1_2(element):
    return (element[1], int(element[2]))


def mikilim_to_wav(path):
    nikiliman = []
    for file in Path(path).glob('**/*'):
        matched = re.match(r'[Pp]art([0-9])-\(([0-9]{1,4})\)\.wav', file.name)
        if not matched:
            print(file.name)
            continue
        part, number = matched.group(1, 2)
        nikiliman.append((file, part, number))

    for i in sorted(nikiliman, key=element_1_2):
        print(i)


if __name__ == '__main__':
    path = sys.argv[1]
    mikilim_to_wav(path)

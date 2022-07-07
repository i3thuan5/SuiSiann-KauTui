from pathlib import Path
import sys


def mikilim_to_wav(path):
    for file in Path(path).glob('**/*'):
        print(file)


if __name__ == '__main__':
    path = sys.argv[1]
    mikilim_to_wav(path)

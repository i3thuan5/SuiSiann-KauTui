from pathlib import Path


def mikilim_to_wav():
    for file in Path('giliau').glob('**/*'):
        print(file)


if __name__ == '__main__':
    mikilim_to_wav()

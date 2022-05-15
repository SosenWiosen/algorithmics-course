import glob
import os


def main():
    files = glob.glob('*')
    files = [file for file in files if file.lower() != file and file.split('.').__len__() == 1]
    for file in files:
        try:
            os.mkdir(file[0])
        except FileExistsError:
            pass
        os.rename(file, f'{file[0]}/{file}')


if __name__ == '__main__':
    main()

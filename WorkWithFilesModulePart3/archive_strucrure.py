# The program should output the files of the desktop.zip
# archive structure and each volume of the file in uncompressed form

from zipfile import ZipFile

size_step = ['B', 'KB', 'MB', 'GB']
def large_units(size):
    step = 0
    while size > 1024:
        size /= 1024
        step += 1
    return round(size), size_step[step]

with ZipFile('desktop.zip') as arch:
    lst_files = [(i.filename, i.file_size) for i in arch.infolist()]
    for file in lst_files:
        print(file[0].split('/'))
        tmp = file[0].split('/')
        if tmp[-1] == '':
            print('  ' * (len(tmp) - 2) + tmp[-2])
        else:
            print('  ' * (len(tmp) - 1) + tmp[-1], *large_units(file[1]))


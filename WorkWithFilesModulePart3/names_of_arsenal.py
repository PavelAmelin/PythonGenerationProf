# Write a program that processes only given JSON files
# and outputs the first and last names of football players
# playing for Arsenal Football Club

from zipfile import ZipFile
import json

with ZipFile('data.zip') as arch:
    lst_files = [i.filename for i in arch.infolist() if 'json' in i.filename and not i.is_dir()]
    Arsenal = []
    for file_name in lst_files:
        try:
            with arch.open(file_name) as f:
                player = json.load(f)
                if player['team'] == 'Arsenal':
                    Arsenal.append((player['first_name'], player['last_name']))
        except:
            pass
    for row in sorted(Arsenal, key=lambda x: (x[0], x[1])):
        print(*row)

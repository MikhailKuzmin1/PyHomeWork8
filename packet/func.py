import os
import json
import csv
import pickle

def size_dir(path):
    size = 0
    for path_f, dirs, files in os.walk(path):
        for i in files:
            fp = os.path.join(path_f, i)
            size += os.path.getsize(fp)
        return size


def direct (path):
    dict_files = {}
    folders = []
    directory = []
    for dirpath, dirnames, filenames in os.walk(path):
        *_, res_dir_name = dirpath.split('\\')
        for dirname in dirnames:
            size_folder = size_dir(os.path.join(dirpath, dirname))
            directory.append((dirname, res_dir_name, size_folder))
            dict_files['Каталог'] = directory
        for filename in filenames:
            folders.append((filename, res_dir_name, os.stat(os.path.join(dirpath,filename)).st_size))
            dict_files['Файл'] = folders
    return dict_files


def to_json(data):
    my_dict = direct(data)
    with open('directory.json', 'w', encoding='UTF-8') as file:
        json.dump(my_dict, file, indent= 2, ensure_ascii=False)


def to_csv(data):
    my_dict = direct(data)
    with open('directory.csv', 'w', encoding='UTF-8') as file:
        for key in my_dict.keys():
            file.write("%s, %s\n" %(key, my_dict[key]))
        # csv_writer = csv.DictWriter(file, dialect='excel', delimiter=';', fieldnames = ['type', 'name', 'path', 'size'])
        # csv_writer.writerows(my_dict)


def to_pickle(data):
    my_dict = direct(data)
    with open('directory.pkl', 'wb') as file:
        pickle.dump(my_dict, file)
        
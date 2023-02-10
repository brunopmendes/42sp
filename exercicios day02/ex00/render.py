import sys, os, re

path = os.curdir


def settings_to_dict():
    file_path = os.path.join(path, 'settings.py')
    
    arq = open(file_path, 'r')
    content = arq.readlines()

    dict_content = {}
    for c in content:
        dict_content[c.split('=')[0].strip()] = c.split('=')[1].strip().replace("'", '')
    return dict_content


def read_temp_file():

    arguments = sys.argv
    arg = arguments[1]
    file_path = os.path.join(path, arg)

    arq = open(file_path, 'r')

    content = arq.read()
    return content


def render_file():
    temp_file = read_temp_file()
    dict_seetings = settings_to_dict()
    temp = temp_file.format(**dict_seetings)

    f = open("myCV.html", "w")
    f.write(temp)
    f.close()

if __name__ == '__main__':
    try:
        render_file()
    except Exception as e:
        print("Erro a partir da variável", e)


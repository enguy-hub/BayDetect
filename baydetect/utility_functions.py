"""This module contains functions which help automate repetitive tasks when using processing functions."""

import os
import fnmatch

""" Brief description of what each utility function does """
"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#uf1 | find_replace_dirname(): function to find and replace the names of multiple folders at once.

#uf2 | find_replace_filename(): function to find and replace the names of multiple files at once.

#uf3 | find_replace_text(): function to find and replace text in multiple files at once.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


# ID: uf1 || find_replace_dirname()
def find_replace_dirname():
    usr_input_dir = input("Enter the absolute path of the parent directory which contains the sub-folders that you wish"
                          " to 'find/replace' their names (end with `/`): ")

    usr_input_find = input("Which part in folder name would you like to change? ")

    usr_input_replaceWith = input("What would you like to replace it to? ")

    for (dirpath, dirnames, filenames) in os.walk(usr_input_dir):
        for idirnames in range(len(dirnames)):
            newname = dirnames[idirnames].replace(usr_input_find, usr_input_replaceWith)
            os.rename(os.path.join(dirpath, dirnames[idirnames]), os.path.join(dirpath, newname))
            dirnames[idirnames] = newname

    return print('Done!')


# ID: uf2 || find_replace_filename()
def find_replace_filename():
    usr_input_dir = input("Enter the absolute path of the parent directory which contains all the files that you wish "
                          "to 'find/replace' their names (end with `/`): ")

    usr_input_find = input("Which part in the filename would you like to change? ")

    usr_input_replaceWith = input("What would you like to replace it to? ")

    for (dirpath, dirnames, filenames) in os.walk(usr_input_dir):
        for ifilenames in range(len(filenames)):
            newname = filenames[ifilenames].replace(usr_input_find, usr_input_replaceWith)
            os.rename(os.path.join(dirpath, filenames[ifilenames]), os.path.join(dirpath, newname))
            filenames[ifilenames] = newname

    return print('Done!')


# ID: uf3 || find_replace_text()
def find_replace_text():
    usr_input_dir = input("Enter the absolute path of the directory which contains all the files that want to "
                          "'find/replace' their text content (end with `/`): ")

    usr_input_pattern = input("What is the common format of the files (eg: '*.json', '*.txt', '*.csv') ? ")

    usr_input_find = input("What part of the text would you like to change? ")

    usr_input_replaceWith = input("What would you like to replace it to? ")

    for path, dirs, files in os.walk(os.path.abspath(usr_input_dir)):
        for filename in fnmatch.filter(files, usr_input_pattern):
            # for filename in files:
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                text = f.read()
                text = text.replace(usr_input_find, usr_input_replaceWith)
            with open(filepath, "w") as f:
                f.write(text)

    return print('Done!')


# if __name__ == '__main__':
    # add_leading_zero_dirnames()

# ID: uf_extra1 || add_leading_zero_dirnames()
"""
def add_leading_zero_dirnames():
    usr_input_dir = 'W:\Laufende Projekte\Schalenwild_Bergwald\Fotofallen\Wolf\Rohdaten\Regular/'

    for dirnames in os.listdir(usr_input_dir):
        print(dirnames)
        prefix, num = dirnames.split('_')
        num = num.zfill(3)
        print(num)
        new_dirnames = prefix + "_" + num
        print(new_dirnames)
        os.rename(os.path.join(usr_input_dir, dirnames), os.path.join(usr_input_dir, new_dirnames))
"""


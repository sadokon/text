#!/usr/bin/env python
# coding: utf-8

import os
import sys

def get_folder(Str):
    Str_re = Str[::-1]
    find_Str = Str_re.find("/")
    Str_re = Str_re[:find_Str]
    Str = Str_re[::-1]
    return Str

def restart_program():
  python = sys.executable
  os.execl(python, python, * sys.argv)

def get_folder_file_info(_dir):
    folder_swt = input("Do you need to hide the parent directory (y/n):")
    result = {}
    for _root, _dir, _files in os.walk(_dir):
        for each_file in _files:
            root = _root.replace("\\", "/")
            if folder_swt == "y":
                root = get_folder(root)
            elif folder_swt != "n":
                print("input error")
                print("restarting......")
                restart_program()
            file_info = os.path.splitext(each_file)
            value = result.get(root)
            if not value:
                result.update({root: [file_info]})
            else:
                value.append(file_info)
    print(result)
    return result


_file_dir = input("please input the path:")
get_folder_file_info(_file_dir)
re_swt = input("do you want to restart(y/n)")
if re_swt == "y":
    restart_program()






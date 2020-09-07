#!/usr/bin/python
# -*- coding:utf-8 -*-
# convert.py
#

import sys
import os
import subprocess

def convert(dirname):

    if os.path.isdir(dirname):
        for pathname, dirs, files in os.walk(dirname):
            if files:
                for f in files:
                    filename = os.path.join(pathname, f)
                    convert_file(filename)
    else:
        convert_file(dirname)

def convert_file(filename):
    
    if filename.find("azw3") != -1 or filename.find("mobi") != -1:
        new_filename = filename
        converted_filename = ""
        if new_filename.find("azw3") != -1:
            converted_filename = new_filename.replace("azw3", "epub")
        if new_filename.find("mobi") != -1:
            converted_filename = new_filename.replace("mobi", "epub")

        commands = []
        commands.append("ebook-convert")
        commands.append(new_filename)
        commands.append(converted_filename)

        subprocess.call(commands)
    
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Please enter directory or file!!")
    else:
        dirname = str(sys.argv[1])
        convert(dirname)
    

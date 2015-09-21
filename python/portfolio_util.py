#!/usr/bin/env python

# data_url.py

import sys
import os
import re
import string
from StringIO import StringIO
from binascii import b2a_base64

# I just think reading or writing a whole file 
# should be a one-liner, so here they are.
 
def read_file(file_name, flags=''):
    f = open(file_name, 'r' + flags)
    data = f.read()
    f.close()
    return data

def write_file(data, file_name, flags=''):
    f = open(file_name, 'w' + flags)
    f.write(data)
    f.close()

# data_url() takes a path to a .jpg file
# and returns a string suitable for inclusion
# as an <img> tag src attribute
#
# TODO: handle image types other than jpeg.
#  - need to be able to determine file type
#  - don't assume you can trust file extention
#  - map file types to the apropriate type string
#    at this point we assume "jpeg"
#
def data_url(img, pretty=False):
    pre = 'data:image/jpeg;base64,'
    uu = b2a_base64(img)
    if pretty:
        uu_io = StringIO(uu)
        width = 60
        x = [pre]
        chunk = uu_io.read(width)
        while len(chunk)>0:
            x.append(chunk)
            chunk = uu_io.read(width)
        return str.join('\n', x).strip()
    else:
        return pre + uu
        
# inline_img_html() wraps a data_url() in some appropriate html,
# including an html comment for any unfortunate souls trying to
# read the output.
# It is currently not used for the movie trailer website
# but I didn't want to throw it out :-)
#
def inline_img_html(img_path):
    s = '<!--\n'
    s += '  uuencode\n'
    s += '  path: ' + img_path + '\n'
    s += '  encoding: base64\n'
    s += '-->\n'
    s += '<img src="'
    s += data_url(img_path, pretty=True)
    s += '\n">'
    return s

def indent(s,n):
    lines = str.split(s, '\n')
    lines = map(lambda(line): ' ' * n + line, lines)
    return str.join('\n', lines)
    
if __name__ == '__main__':
    for img_path in sys.argv[1:]:
        base = os.path.splitext(img_path)[0]
        img = read_file(img_path, 'b')
        write_file(data_url(img), base + "_data_url.src")
        write_file(inline_img_html(img), base + "_data_url.html")


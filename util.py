# -*- coding: utf-8
import os, subprocess
from tempfile import NamedTemporaryFile

def try_compress_png(raw_img, format):
    ''' use pngquant to compress:https://github.com/pornel/pngquant'''
    need_compress = format!='gif'
    if not need_compress: return raw_img
    if not os.path.exists(raw_img.name): return raw_img
    tmp_file = NamedTemporaryFile()
    return tmp_file if not subprocess.call('pngquant --force %s -o %s' \
        % (raw_img.name, tmp_file.name), shell=True) else raw_img
# -*- coding: utf-8
import os
import subprocess
from tempfile import NamedTemporaryFile
import dateutil.parser
import datetime


def try_compress_png(raw_img, format):
    ''' use pngquant to compress:https://github.com/pornel/pngquant'''
    need_compress = format != 'gif'
    if not need_compress:
        return raw_img
    if not os.path.exists(raw_img.name):
        return raw_img
    tmp_file = NamedTemporaryFile()
    return tmp_file if not subprocess.call('pngquant --force %s -o %s'
                                           % (raw_img.name, tmp_file.name), shell=True) else raw_img


def get_time(time_str):
    time_parser = dateutil.parser.parse(time_str) + datetime.timedelta(hours=8)
    return time_parser.strftime('%Y-%m-%d %H:%M:%S')

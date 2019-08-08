#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from header import RSA_CONTROL
from header import PUBLIC_KEY_PATH
from header import PRIVATE_KEY_PATH
from header import RSA
from header import os


__all__ = ['generate']
__author__ = 'Yee_172'
__date__ = '2019/08/08'


def generate():
    folder_name = os.path.dirname(PUBLIC_KEY_PATH)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    folder_name = os.path.dirname(PRIVATE_KEY_PATH)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    key = RSA.generate(RSA_CONTROL)

    with open(PUBLIC_KEY_PATH, 'wb') as f:
        f.write(key.publickey().exportKey('PEM'))

    with open(PRIVATE_KEY_PATH, 'wb') as f:
        f.write(key.exportKey('PEM'))


if __name__ == '__main__':
    generate()

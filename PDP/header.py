#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Cipher import PKCS1_OAEP
import os


__author__ = 'Yee_172'
__date__ = '2019/08/08'


ENCODING = 'utf-8'
PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC_KEY_PATH = os.path.join(PATH, 'key/public_key.pem')
PRIVATE_KEY_PATH = os.path.join(PATH, 'key/private_key.pem')
ENCRYPTED_PATH = os.path.join(PATH, 'encrypted')
ORIGIN_PATH = os.path.join(PATH, 'origin')
RSA_CONTROL = 2048
SECTION = 200
BLOCK = 100
SPLITER = b'|--|'
SHOW_LENGTH = 40


def hyphen_shower(info):
    print('-' * SHOW_LENGTH)
    if isinstance(info, str):
        print(info.center(SHOW_LENGTH))
    else:
        for each_info in info:
            print(each_info.center(SHOW_LENGTH))
    print('-' * SHOW_LENGTH)


def red_print(info):
    print('\033[31m' + info + '\033[0m')


def green_print(info):
    print('\033[32m' + info + '\033[0m')


def error_shower(info, exist_after_show=True):
    print('\033[31m')
    hyphen_shower(info)
    print('\033[0m')
    if exist_after_show:
        exit()


def success_shower(info):
    print('\033[32m')
    hyphen_shower(info)
    print('\033[0m')


def initialize():
    encryptor = ''
    decryptor = ''
    load_error = []
    if os.path.exists(PUBLIC_KEY_PATH):
        try:
            with open(PUBLIC_KEY_PATH, 'rb') as f:
                public_key = RSA.importKey(f.read())
                encryptor = PKCS1_OAEP.new(public_key)
        except:
            load_error.append('Warning: Public key not valid'.ljust(SHOW_LENGTH))
    else:
        load_error.append('Warning: Public key not found'.ljust(SHOW_LENGTH))


    if os.path.exists(PRIVATE_KEY_PATH):
        try:
            with open(PRIVATE_KEY_PATH, 'rb') as f:
                private_key = RSA.importKey(f.read())
                decryptor = PKCS1_OAEP.new(private_key)
        except:
            load_error.append('Warning: Private key not valid'.ljust(SHOW_LENGTH))
    else:
        load_error.append('Warning: Private key not found'.ljust(SHOW_LENGTH))


    if load_error:
        error_shower(load_error, False)

    return encryptor, decryptor


encryptor, decryptor = initialize()

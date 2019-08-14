#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from header import ENCODING
from header import ENCRYPTED_PATH
from header import ORIGIN_PATH
from header import SECTION
from header import BLOCK
from header import SPLITER
from header import encryptor
from header import os


__all__ = ['encrypt', 'encrypt_for_file']
__author__ = 'Yee_172'
__date__ = '2019/08/08'


def _encrypt(message, encoding=ENCODING):
    if not isinstance(message, bytes):
        if not isinstance(message, str):
            message = str(message)
        message = bytes(message, encoding=encoding)
    return SPLITER.join(map(encryptor.encrypt, [message[i * SECTION:(i + 1) * SECTION] for i in range((len(message) - 1) // SECTION + 1)]))


def beautify(context):
    return '\n'.join(context[i * BLOCK:(i + 1) * BLOCK] for i in range((len(context) - 1) // BLOCK + 1))


def encrypt(message, encoding=ENCODING):
    return beautify(_encrypt(message, encoding=encoding).hex()) + '\n'


def _encrypt_path_check(dir_name):
    dir_path = os.path.join(ENCRYPTED_PATH, dir_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def encrypt_for_file(file_name, encoding=ENCODING):
    try:
        with open(os.path.join(ORIGIN_PATH, file_name), 'r', encoding=encoding) as f:
            content = f.read()
        with open(os.path.join(ENCRYPTED_PATH, file_name), 'w', encoding=encoding) as f:
            f.write(encrypt(content, encoding=encoding))
    except FileNotFoundError as exception:
        raise Exception('No such file or directory')
    except IsADirectoryError as exception:
        raise Exception('Is a directory')
    except UnicodeDecodeError as exception:
        raise Exception('Unicode decode error')
    except Exception as exception:
        raise Exception(exception.__class__.__name__)


if __name__ == '__main__':
    print(encrypt('encrypt'), end='')

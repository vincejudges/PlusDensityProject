#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from header import ENCODING
from header import ENCRYPTED_PATH
from header import ORIGIN_PATH
from header import SPLITER
from header import decryptor
from header import os


__all__ = ['decrypt', 'decrypt_for_file']
__author__ = 'Yee_172'
__date__ = '2019/08/08'


def _decrypt(ciphertext):
    return b''.join(map(decryptor.decrypt, ciphertext.split(SPLITER)))


def reverse_beautify(context):
    return ''.join(context.split('\n'))


def decrypt(ciphertext, encoding=ENCODING):
    return _decrypt(bytes.fromhex(reverse_beautify(ciphertext))).decode(encoding=encoding)


def decrypt_for_file(file_name, encoding=ENCODING):
    try:
        with open(os.path.join(ENCRYPTED_PATH, file_name), 'r', encoding=encoding) as f:
            encrypted_content = f.read()
    except FileNotFoundError as exception:
        raise Exception('No such file or is a directory')
    except UnicodeDecodeError as exception:
        raise Exception('Unicode decode error')
    except Exception as exception:
        raise Exception(exception.__class__.__name__)
    try:
        with open(os.path.join(ORIGIN_PATH, file_name), 'w', encoding=encoding) as f:
            f.write(decrypt(encrypted_content, encoding=encoding))
    except Exception as exception:
        raise Exception(exception.__class__.__name__)


if __name__ == '__main__':
    from encrypt import encrypt
    print(decrypt(encrypt('decrypt')))

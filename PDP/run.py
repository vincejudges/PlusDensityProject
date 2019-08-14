#/usr/bin/env python3
# -*- coding: utf-8 -*-
from header import ENCRYPTED_PATH
from header import ORIGIN_PATH
from header import hyphen_shower
from header import error_shower
from header import success_shower
from header import initialize
from header import encryptor
from header import decryptor
from header import os
from key_generator import generate
from encrypt import encrypt
from encrypt import encrypt_for_file
from encrypt import _encrypt_path_check
from decrypt import decrypt
from decrypt import decrypt_for_file
from decrypt import _decrypt_path_check


__all__ = []
__author__ = 'Yee_172'
__date__ = '2019/08/08'


if __name__ == '__main__':
    def _file_operation(folder_path_header, operation, checker=None):
        counter = [0]
        def _dfs_file_operation(folder_path):
            current_path = os.path.join(folder_path_header, folder_path)
            if checker is not None:
                checker(folder_path)
            for file_name in os.listdir(current_path):
                current_file = os.path.join(folder_path, file_name)
                if file_name.startswith('.'):
                    if not counter[0]:
                        print('\n\033[31mIgnore list:\033[0m')
                    counter[0] += 1
                    print('[{:2d}] {}'.format(counter[0], current_file))
                    continue
                current_file_absolute_path = os.path.join(folder_path_header, current_file)
                if os.path.isfile(current_file_absolute_path):
                    operation(current_file)
                elif os.path.isdir(current_file_absolute_path):
                    _dfs_file_operation(current_file)
        _dfs_file_operation('')


    hyphen_shower('Welcome to PDP')
    try:
        while True:
            print('Use KeyboardInterrupt to exit')
            print('{} \033[32m{}\033[0m {}'.format('Only', 'green options', 'are available'))
            print()

            print('\033[32m{}\033[0m'.format('[ 1] Generate a new pair of key'))

            print('\033[32m' if encryptor else '\033[31m', end='')
            print('[ 2] Encrypt  in      terminal')
            print('[ 3] Encrypt  single  file')
            print('[ 4] Encrypt  all     files\033[0m')

            print('\033[32m' if decryptor else '\033[31m', end='')
            print('[ 5] Decrypt  in      terminal')
            print('[ 6] Decrypt  single  file')
            print('[ 7] Decrypt  all     files\033[0m')
            n = input('Input a number to choose [1 - 7]: ')
            try:
                n = int(n)
            except:
                error_shower('Invalid input', exist_after_show=False)
                continue
            if not 0 < n < 8:
                error_shower('Input not in the range', exist_after_show=False)
                continue
            if n == 1:
                generate()
                success_shower('A new pair of key created')
            if n == 2:
                if not encryptor:
                    error_shower('Public key unavailable', exist_after_show=False)
                    continue
                print('\nUse KeyboardInterrupt as a signal of finish')
                print('Message in the KeyboardInterrupt line would')
                print('    not be considered as input')
                print('\033[32m{}\033[0m'.format('Please input your message below:'))
                message = []
                try:
                    while True:
                        message.append(input())
                except KeyboardInterrupt:
                    message = '\n'.join(message)
                    try:
                        encrypted_message = encrypt(message)
                    except ValueError as exception:
                        error_shower(str(exception).replace('.', ''), exist_after_show=False)
                        continue
                    except Exception as exception:
                        error_shower(exception.__class__.__name__, exist_after_show=False)
                        continue
                    else:
                        print('\nEncrypted message showed below:')
                        print(encrypted_message)
                except Exception as exception:
                    error_shower(exception.__class__.__name__, exist_after_show=False)
                    continue
            if n == 3:
                if not encryptor:
                    error_shower('Public key unavailable', exist_after_show=False)
                    continue
                file_name = input('Please input file name: ')
                try:
                    encrypt_for_file(file_name)
                except Exception as exception:
                    error_shower(exception.args, exist_after_show=False)
                    continue
                else:
                    success_shower('{} has been encrypted'.format(file_name))
            if n == 4:
                if not encryptor:
                    error_shower('Public key unavailable', exist_after_show=False)
                    continue
                try:
                    _file_operation(ORIGIN_PATH, encrypt_for_file, _encrypt_path_check)
                except Exception as exception:
                    error_shower(exception.args, exist_after_show=False)
                    continue
                else:
                    success_shower('all available files have been encrypted')
            if n == 5:
                if not decryptor:
                    error_shower('Private key unavailable', exist_after_show=False)
                    continue
                print('\nUse KeyboardInterrupt as a signal of finish')
                print('Message in the KeyboardInterrupt line would')
                print('    not be considered as input')
                print('\033[32m{}\033[0m'.format('Please input your encrypted message below:'))
                encrypted_message = []
                try:
                    while True:
                        encrypted_message.append(input())
                except KeyboardInterrupt:
                    encrypted_message = '\n'.join(encrypted_message)
                    try:
                        message = decrypt(encrypted_message)
                    except ValueError as exception:
                        error_shower(str(exception).replace('.', ''), exist_after_show=False)
                        continue
                    except Exception as exception:
                        error_shower(exception.__class__.__name__, exist_after_show=False)
                        continue
                    else:
                        print('\nOriginal message showed below:')
                        print(message)
                        print()
                except Exception as exception:
                    error_shower(exception.__class__.__name__, exist_after_show=False)
                    continue
            if n == 6:
                if not decryptor:
                    error_shower('Private key unavailable', exist_after_show=False)
                    continue
                file_name = input('Please input file name: ')
                try:
                    decrypt_for_file(file_name)
                except Exception as exception:
                    error_shower(exception.args, exist_after_show=False)
                    continue
                else:
                    success_shower('{} has been decrypted'.format(file_name))
            if n == 7:
                if not decryptor:
                    error_shower('Private key unavailable', exist_after_show=False)
                    continue
                try:
                    _file_operation(ENCRYPTED_PATH, decrypt_for_file, _decrypt_path_check)
                except Exception as exception:
                    error_shower(exception.args, exist_after_show=False)
                    continue
                else:
                    success_shower('all available files have been decrypted')
    except KeyboardInterrupt:
        success_shower('Exit successfully')
    except Exception as exception:
        error_shower('Unknown exit way: {}'.format(exception.args or 'Unknown'))

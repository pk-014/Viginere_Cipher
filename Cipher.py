#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 25 21:19:31 2025

@author: Asad
"""

source_dict = {
    0:'a',
    1:'b',
    2:'c',
    3:'d',
    4:'e',
    5:'f',
    6:'g',
    7:'h',
    8:'i',
    9:'j',
    10:'k',
    11:'l',
    12:'m',
    13:'n',
    14:'o',
    15:'p',
    16:'q',
    17:'r',
    18:'s',
    19:'t',
    20:'u',
    21:'v',
    22:'w',
    23:'x',
    24:'y',
    25:'z'
    }

class ViginereCipher:
    """
   Vigenère Cipher encryption and decryption.

   The Vigenère cipher (French pronunciation: [viʒnɛːʁ]) is a method 
   of encrypting alphabetic text where each letter of the plaintext 
   is encoded with a different Caesar cipher, whose increment is determined 
   by the corresponding letter of another text, the key. 

   Methods:
       encrypt(text: str, key: str) -> str:
           Encrypts the given plain text using the Vigenère Cipher with the provided key.
       
       decrypt(text: str, key: str) -> str:
           Decrypts the given ciphered text using the Vigenère Cipher with the provided key.
   """
    def encrypt(self, text, key):
        """
       Encrypts the given plain text using the Vigenère Cipher.

       Parameters:
           text (str): The plain text to be encrypted.
           key (str): The keyword used for encryption (length must be equal to plain text).

       Returns:
           str: The encrypted ciphertext.

       Example:
           >>> cipher = VigenereCipher()
           >>> cipher.encrypt("HELLO", "KEYKEY")
           'RIJVS'
       """
        cipher_text = ""
        try:
            for x,char in enumerate(text):
                key_char = key[x]
                cipher_char = ([x for x in source_dict.keys() if source_dict[x]==char][0] + [x for x in source_dict.keys() if source_dict[x]==key_char][0])%26
                cipher_text += source_dict[cipher_char]
            return cipher_text
        except Exception as e:
            print("An error occurred, please read the documentation.")
            print(e)
    def decrypt(self, text, key):
        """
       Decrypts the given ciphertext using the Vigenère Cipher.

       Parameters:
           text (str): The encrypted text (ciphertext).
           key (str): The keyword used for decryption (length must be equal/greater to chipertext).

       Returns:
           str: The decrypted plain text.

       Example:
           >>> cipher = VigenereCipher()
           >>> cipher.decrypt("RIJVS", "KEYKEY")
           'HELLO'
       """
        plain_text = ""
        try:
            for x,char in enumerate(text):
                key_char = key[x]
                plain_char = ([x for x in source_dict.keys() if source_dict[x]==char][0] - [x for x in source_dict.keys() if source_dict[x]==key_char][0])%26
                plain_text += source_dict[plain_char]
            return plain_text
        except Exception as e:
            print("An error occurred, please read the documentation.")
            print(e)
            


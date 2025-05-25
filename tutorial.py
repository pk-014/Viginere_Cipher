#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 25 22:41:54 2025

@author: Asad
"""

from Cipher import ViginereCipher

cipher = ViginereCipher()

print("Original Text: helloworld \nCipher Text: ",cipher.encrypt('helloworld', 'dingchingming'))
print("Cipher Text : kmyrqdwerp \nOriginal Text:  ",cipher.decrypt('kmyrqdwerp', 'dingchingming'))
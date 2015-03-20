# -*- coding: utf-8 -*-


import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

__title__ = 'AESHelper'
__version__ = '0.0.1'
__author__ = 'Franco Correa'
__license__ = 'GPLv3'
__copyright__ = 'Copyright 2015 AtomLife and Franco Correa'

class AESCipher(object):

    # AESCipher("<clave-privada-de-encriptado>")
    def __init__(self, key):
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

def aes_encrypt(secret_key, str_to_encrypt):
    cr = AESCipher(secret_key)
    return cr.encrypt(str_to_encrypt)

def aes_decrypt(secret_key, str_to_decrypt):
    cr = AESCipher(secret_key)
    return cr.decrypt(str_to_decrypt)

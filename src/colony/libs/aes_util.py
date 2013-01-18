#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Colony Framework
# Copyright (c) 2008-2012 Hive Solutions Lda.
#
# This file is part of Hive Colony Framework.
#
# Hive Colony Framework is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hive Colony Framework is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hive Colony Framework. If not, see <http://www.gnu.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2012 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import os

import Crypto.Cipher.AES

BLOCK_SIZE = 16
""" The block size to be used for the post operation
should not be too small or security issues may arise """

class AesCipher:
    """
    The class responsible for a proper encryption
    and decryption system for the aes system.

    The aes include the padding infra-structure for
    according to pkcs5.

    @see: http://tools.ietf.org/html/rfc2898
    """

    def __init__(self, key = None):
        """
        Constructor of the class.

        @type key: String
        @param key: The symmetric key (secret) to be used
        in the aes encryption, in case it's not defined
        a new random key will be created.
        """

        self.key = key or os.urandom(BLOCK_SIZE)

    def encrypt(self, raw):
        """
        Encrypts the provided raw string value according
        to the aes and pkcs5 specifications.

        @type raw: String
        @param raw: The raw string value to be used in
        the encryption process.
        @rtype: String
        @return: The encrypted string according to the aes
        cryptographic system in ecb mode.
        """

        raw = self.pad(raw)
        cipher = Crypto.Cipher.AES.new(self.key, Crypto.Cipher.AES.MODE_ECB)
        return cipher.encrypt(raw)

    def decrypt(self, encoded):
        """
        Decrypts the provided encoded (encrypted) string
        into the raw value.

        @type encoded: String
        @param encoded: The encrypted string to be used
        in the decryption process, should be padded according
        to the pkcs5 schema.
        @rtype String
        @return: The decrypted string according to the aes
        cryptographic system in ecb mode.
        """

        cipher = Crypto.Cipher.AES.new(self.key, Crypto.Cipher.AES.MODE_ECB)
        decoded = cipher.decrypt(encoded)
        return self.unpad(decoded)

    def pad(self, value):
        """
        Adds the pkcs5 padding to the provided value
        it should add all the extra padding values to it.

        @type value: String
        @param value: The base value for which the padded
        characters will be added.
        @rtype: String
        @return: The pkcs5 padded string with the padding
        characters added to it.
        """

        remaining = BLOCK_SIZE - len(value) % BLOCK_SIZE
        padding = remaining * chr(remaining)
        return value + padding

    def unpad(self, value):
        """
        Removes the pkcs5 padding from the provided value
        it should remove all the extra padding values from it.

        @type value: String
        @param value: The padded value from which all the
        extra padding characters.
        @rtype: String
        @return: The sanitized string without the extra
        padding characters.
        """

        last = value[-1]
        pad_size = ord(last)
        return value[:-pad_size]

    def block_size(self):
        return BLOCK_SIZE

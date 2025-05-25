# Vigenère Cipher encryption and decryption.

   The Vigenère cipher (French pronunciation: [viʒnɛːʁ]) is a method 
   of encrypting alphabetic text where each letter of the plaintext 
   is encoded with a different Caesar cipher, whose increment is determined 
   by the corresponding letter of another text, the key. 

### Methods:
       - encrypt(text: str, key: str) -> str:
           Encrypts the given plain text using the Vigenère Cipher with the provided key.
       
       - decrypt(text: str, key: str) -> str:
           Decrypts the given ciphered text using the Vigenère Cipher with the provided key.

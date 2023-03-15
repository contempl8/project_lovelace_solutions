#!/usr/bin/env python3

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def break_caesar_cipher(ciphertext, known_word):
    for i in range(len(alphabet)):
        cipherbet=alphabet[i:]+alphabet[:i]
        plaintext=""
        for letter in ciphertext:
            if letter == " ":
                plaintext+=" "
            else:
                try:
                    idx=alphabet.index(letter)
                    plaintext+=cipherbet[idx]
                except ValueError:
                    plaintext+=letter
        if known_word.upper() in plaintext:
            return plaintext.lower()


print(break_caesar_cipher("QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD","fox"))
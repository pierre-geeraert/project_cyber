from itertools import cycle

name_file_crypted = 'FICHIERS/PB.txt'
name_file_decrypted = 'FICHIERS/PA_decrypted.txt'
key="b'CHFYJQ'"

def xor_operation(data, key):
    return bytes(a ^ b for a, b in zip(data, cycle(key)))

with open(name_file_crypted, 'rb') as encrypted_file, open(name_file_decrypted, 'wb') as decrypted_file:
    decrypted_file.write(xor_operation(encrypted_file.read(), b'CHFYJQ'))

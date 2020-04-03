import sys
from itertools import cycle

name_file_crypted = 'FICHIERS/PB.txt'
name_file_decrypted = 'FICHIERS/PA_decrypted.txt'
key=b'CHFYJQ'

def xor_operation(data, key):
    return bytes(a ^ b for a, b in zip(data, cycle(key)))


def main(name_file_crypted_in,key_in,name_file_decrypted_out):
    with open(name_file_crypted_in, 'rb') as encrypted_file, open(name_file_decrypted_out, 'wb') as decrypted_file:
        decrypted_file.write(xor_operation(encrypted_file.read(), key_in))


if __name__ == "__main__":
    main(name_file_crypted_in=name_file_crypted,key_in=key,name_file_decrypted_out=name_file_decrypted)

#main(name_file_crypted_in='FICHIERS/PA.txt',key_in=key,name_file_decrypted_out='FICHIERS/PA_decrypted.txt')
main(key_in=sys.argv[1],name_file_crypted_in=sys.argv[2],name_file_decrypted_out=sys.argv[3])
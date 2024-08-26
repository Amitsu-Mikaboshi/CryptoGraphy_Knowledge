# I know the file formate that will help me to find the secrect unknown salt
from pwn import *
cipher_data = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d') # this will output byte from the hexstring
flag_byte = 'crypto{'.encode('utf-8') #need byte for xor to get better result, so turn the string into byte
secrect_keybyte = xor(flag_byte,cipher_data) #print and creck the repeatent for salt
result = xor(secrect_keybyte[0],cipher_data).decode('utf-8') # put the salt for result and decode the byte
print(result)
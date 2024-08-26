from pwn import *
k1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
k2_3 = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
flag_byte = xor(bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'),k1,k2_3)
flag = flag_byte.decode('utf-8')
print(flag)
# turning hex into bytes makes easy to calculate in printable form
# so converting hexstrin into bytes then xor the things and return the byte into readable formate
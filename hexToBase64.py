import base64
hex_string = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
byte_data = bytes.fromhex(hex_string) #this line makes bytes from hex
#and we need bytes data to encode and decode
cipher_bytes = base64.b64encode(byte_data)
cipher = cipher_bytes.decode('utf-8') #resolve the bytes into printable formate
print(cipher)
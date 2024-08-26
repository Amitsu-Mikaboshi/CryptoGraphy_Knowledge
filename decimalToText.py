# general and basic process to convert
decimal_number = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
hex_text = hex(decimal_number) #it contains 0x and its type is string tho
withoutPrefix = hex_text.replace('0x','')
byteFromHex = bytes.fromhex(withoutPrefix) #it will split the hex in peice and make byte
result = byteFromHex.decode('utf-8')



# easier way to process the convert
from Crypto.Util.number import *
deci =  11515195063862318899931685488813747395775516287289682636499965282714637259206269
bytes_data = long_to_bytes(deci)
result_2 = bytes_data.decode('utf-8')
print(result_2)
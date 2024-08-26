import base64
cipher = 'SGVsbG8sIFdvcmxkIQ=='
# we need to convert in byte data inorder to encoding and decoding
cipher_data = cipher.encode('utf-8') #this will turn the string into byte data
plain_data = base64.b64decode(cipher_data) #decode the byte data and the output also in byte
plain = plain_data.decode('utf-8')
print(plain)
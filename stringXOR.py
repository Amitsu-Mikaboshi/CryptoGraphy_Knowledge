#easy way to solve this without library
cipher = 'label'
print(''.join(chr(ord(x)^13)for x in cipher)) 


# without library step by step
ord_list = [ord(x) for x in cipher] # for loop make list, so we use [] to make it list
after_Xor = [(x ^ 13) for x in ord_list]
char_convert = [chr(x) for x in after_Xor]
string = ''.join(char_convert) # join each element from a list and make string
print(string)
string="MANAV {}"
print(string.format('SHAH'))
print(string.capitalize())#capitalize first letter of a word
print(string.center(30,'*'))#change the length of string to 30 characters
print(string.casefold())#same as lower()
print(string.count(' ',1,))#returns occurunce of a perticular substring
print(string.endswith('SHAH'))#returns true if the string ends with specified substring else False
print(string.encode(encoding='ascii',errors='strict'))
print(string.find('SHAH'))

dict={'name':'manav','sirname':'shah','father':'kaushal'}
print(' '.join(dict.values()))
"""
Split, Join, Enumerate em Python
* Split - Dividi uma string # str
* Count - Conta quantas palavras existem em uma lista
* strip - Elimina espaço tanto no início como no final da frase.
* Join - Junta elementos de uma lista # str
* Enumerate - Enumera elementos da lista # iteráveis
"""
string = 'O Brasil é o país do futebol, o Brasil é penta campeão e é top demais.'
print(f'String: {string}')
print(f'String: {string.split()}')
string = ''.join(string)
print(f'String: {string}')
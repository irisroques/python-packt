"""
encontra o maior numero em uma lista de numeros
"""

l = [4,2,7,3]
maior = 0

for number in l:
    if number > maior:
        maior = number

print(maior)
"""

Implemente uma função que formata um programa em C.
O código será fornecido numa única linha e deverá introduzir
um '\n' após cada ';', '{', ou '}' (com excepção da última linha).
No caso do '{' as instruções seguintes deverão também estar identadas
2 espaços para a direita.

"""
import re

aux = "{}"

def chaveta(str):
    for elem in str:
        if elem in aux:
            return True
    return False

def formata(codigo):
    strpd = re.sub(' +', ' ', codigo)
    strpd = re.sub('; +', ';', codigo)
    idx = 0
    res = ""
    
    if chaveta(strpd):
        for char in strpd:
            if char == ';':
                if idx != len(strpd)-1 and idx != len(strpd)-2:
                    res += char + '\n' +  '  '
                    idx += 1
                else:
                    res += char + '\n'
                    idx += 1
            elif char == '{':
                res += char + '\n' + '  '
                idx += 1
            elif char == '}':
                res += char
                idx += 1
            else:
                res += char
                idx += 1
        return res
    
    else:
        for char in strpd:
            if char == ';':
                if idx != len(strpd)-1:
                    res += char + '\n'
                    idx += 1
                else:
                    res += char
                    idx += 1
            elif char == '{':
                res += char + '\n'
                idx += 1
            elif char == '}':
                res += char
                idx += 1
            else:
                res += char
                idx += 1
        return res

#Nota:40%
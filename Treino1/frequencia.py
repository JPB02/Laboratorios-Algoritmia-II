'''
Neste problem pretende-se que defina uma função que, dada uma string com palavras, 
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas 
por ordem alfabética.
'''

def frequencia(texto):
    r = []
    dict = {}
    x = texto.split()
    for word in x:
        dict.update({word:x.count(word)})
    print(dict)
    sorted_ = sorted(dict)
    sorted_.sort(key = lambda x: dict[x], reverse = True)
    return sorted_
        
        
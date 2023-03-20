'''
Pretende-se que implemente uma função que detecte códigos ISBN inválidos. 
Um código ISBN é constituído por 13 digitos, sendo o último um digito de controlo.
Este digito de controlo é escolhido de tal forma que a soma de todos os digitos, 
cada um multiplicado por um peso que é alternadamente 1 ou 3, seja um múltiplo de 10.
A função recebe um dicionário que associa livros a ISBNs,
e deverá devolver a lista ordenada de todos os livros com ISBNs inválidos.
'''

def formula(str_nums):
    sum_ = 0
    idx = 0
    for num in str_nums:
        if idx % 2 == 0:
            sum_ += int(num)
            idx += 1
        else:
            sum_ += 3*int(num)
            idx += 1
    return sum_ % 10 == 0

def isbn(livros): 
    invalidos = []
    for book in livros:
        if len(livros.get(book)) != 13:
            invalidos.append(book) 
        elif not formula(livros.get(book)):
            invalidos.append(book)
    return sorted(invalidos)
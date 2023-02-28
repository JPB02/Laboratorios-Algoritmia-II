'''
Neste problema prentede-se que implemente uma função que calcula o rectângulo onde se movimenta um robot.

Inicialmente o robot encontra-se na posição (0,0) virado para cima e irá receber uma sequência de comandos numa string.
Existem quatro tipos de comandos que o robot reconhece:
  'A' - avançar na direcção para o qual está virado
  'E' - virar-se 90º para a esquerda
  'D' - virar-se 90º para a direita 
  'H' - parar e regressar à posição inicial virado para cima
  
Quando o robot recebe o comando 'H' devem ser guardadas as 4 coordenadas (minímo no eixo dos X, mínimo no eixo dos Y, máximo no eixo dos X, máximo no eixo dos Y) que definem o rectângulo 
onde se movimentou desde o início da sequência de comandos ou desde o último comando 'H'.

A função deve retornar a lista de todas os rectangulos (tuplos com 4 inteiros)

      (0,1)
        |
(-1,0)__|__ (1,0)
        |
        |
      (0,-1)
'''

def robot(comandos):
    pos = {0:(0,1), 1:(-1,0), 2:(0,-1), 3:(1,0)}

    res = []
    
    if comandos[-1] != 'H':
      com = comandos.split('H')
    
    else:
      com = comandos.split('H')
      com.pop()
    
    for instruction in com:
      direcao = 0
      cord = [(0,0)]
      val = {'x':0, 'y':0}
      for char in instruction:
        
        if char == 'E':
          direcao = (direcao+1)%4
        
        elif char == 'D':
          direcao = (direcao-1)%4
        
        elif char == 'A':
          val['x'] += (pos[direcao])[0]
          val['y'] += (pos[direcao])[1]
          cord.append((val['x'],val['y']))
      
      min_x = sorted(cord,key=lambda x: x[0])[0][0]
      min_y = sorted(cord,key=lambda x: x[1])[0][1]
      max_x = sorted(cord,key=lambda x: x[0],reverse=True)[0][0]
      max_y = sorted(cord,key=lambda x: x[1],reverse=True)[0][1]
      res.append(tuple((min_x,min_y,max_x,max_y)))
    return res

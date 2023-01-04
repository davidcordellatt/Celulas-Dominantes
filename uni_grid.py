import random

def uni_grid(grid: list):

  # Verificando tamaño de la Cuadricula
  min_len = 3
  if grid == [[]]:
    # Autocompletado para evitar errores
    for _ in range(min_len):
      aux = random.randint(0, 21)
      grid[0].append(aux)
  
  
  
  

  #Analizando cuadricula
  M = len(grid[0])
  idx = 0
  dom = 0
  while idx < M:
    if idx == 0:
      #Primer Digito
      if grid[0][idx] > grid[0][idx + 1]:
        print(f'Primer digito, {grid[0][idx]}')
        dom += 1

    
    if idx == M - 1:
      #Ultimo Digito
      if grid[0][-2] < grid[0][-1]:
        print(f'Ultimo Digito, {grid[0][-1]}')
        dom += 1 

    
    if idx > 0 and idx < M - 1:
      #Intermedio
      if grid[0][idx] > grid[0][idx - 1] and grid[0][idx] > grid[0][idx + 1]:
        print(f'Intermedio, {grid[0][idx]}')
        dom += 1
        
    idx += 1
          
  return dom

if __name__ == '__main__':
  example = [[2, 2, 2]]

  print('En una array unidimencional, como:')

  print('---' * 5)
  for i in example:
    print(*i)
  print('---' * 5)
    
  print('No hay dominantes dado que todos los digitos son iguales.' , '\n')

  example = [[0, 2, 0]]

  print('En una array unidimencional, como:')
  
  print('---' * 5)
  for i in example:
    print(*i)
  print('---' * 5)
  
  print(f'Hay {uni_grid(example)} dominantes. El 2 perteneciente al index 1', '\n')

  example = [[5, 0, 3, 0, 2, 0, 7]]

  print('En una array unidimencional, como:')
  
  print('---' * 5)
  for i in example:
    print(*i)
  print('---' * 5)
  
  print(f'Hay {uni_grid(example)} dominantes. 5, 3, 2 y 7 en su respectiva posición.')


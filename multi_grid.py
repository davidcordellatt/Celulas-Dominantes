import random

def multi_grid(grid):
  # Autocompletado para evitar errores
  max_len = max([len(col) for col in grid])
  max_num = max([max(col) for col in grid if col !=[]])
  for col in grid:
    if len(col) < max_len:
      while len(col) < max_len:
        col.append(random.randint(1, max_num))
        
  dom = 0
  n = len(grid)
  m = len(grid[0])
  
  for col in range(n):
    for idx in range(m):
    #Comienzo
      if idx == 0:
        #Primer digito del comienzo
        if col == 0:
          start = grid[0][0] 
          if start > grid[0][1] and start > grid[1][0] and start > grid[1][1]:
            print(f'Izquierda Arriba, {start}')
            dom += 1
        
        #Digitos intermedios del comienzo
        if col > 0 and col < n - 1:
          mid = grid[col][idx]
          if mid > grid[col - 1][idx] and mid > grid[col + 1][idx] and mid > grid[col][idx + 1] and mid > grid[col - 1][idx + 1] and mid > grid[col + 1][idx + 1]:
            print(f'Intermedio Izquierda, {mid}')
            dom += 1
          
        #Digito final del comienzo
        if col == n - 1:
          end = grid[-1][0]
          if end > grid[-1][1] and end > grid[-2][1] and end > grid[-2][0]:
            print(f'Izquierda abajo, {end}')
            dom += 1

      # Final 
      elif idx == m - 1:
        
        if col == 0:
        #Primer digito del final
          start = grid[0][-1]
          if start > grid[0][-2] and start > grid[1][-1] and start > grid[1][-2]:
            print(f'Derecha Arriba, {start}')
            dom += 1

        #Digitos intermedios del final
        if col > 0 and col < n - 1:
          mid = grid[col][-1]
          if mid > grid[col][-2] and mid > grid[col - 1][-1] and mid > grid[col - 1][-2] and mid > grid[col + 1][-1] and mid > grid[col + 1][-2]:
            print(f'Intermedio Derecha, {mid}')
            dom += 1

        #Ultimo digito del final
        if col == n - 1:
          end = grid[-1][-1]
          if end > grid[-1][-2] and end > grid[-2][-1] and end > grid[-2][-2]:
            print(f'Derecha abajo, {end}')
            dom += 1

      #Top line
      elif idx > 0 and idx < m - 1 and col == 0:
        top = grid[col][idx]
        if top > grid[col][idx - 1] and top > grid[col][idx + 1] and top > grid[col + 1][idx] and top > grid[col + 1][idx - 1] and top > grid[col + 1][idx + 1]:
          print(f'Top line, {top}')
          dom +=1

      #Under line
      elif idx > 0 and idx < m - 1 and col == n - 1:
        under = grid[col][idx]
        if under > grid[col][idx - 1] and under > grid[col][idx + 1] and under > grid[col - 1][idx] and under > grid[col - 1][idx - 1] and under > grid[col - 1][idx + 1]:
          print(f'Under line, {under}')
          dom +=1




        
      else:
        cross = grid[col][idx]
        if cross > grid[col][idx - 1] and cross > grid[col][idx + 1] and cross > grid[col - 1][idx] and cross > grid[col + 1][idx] and cross > grid[col + 1][idx + 1] and cross > grid[col + 1][idx - 1] and cross > grid[col - 1][idx - 1] and cross > grid[col - 1][idx + 1]:
            print(f'Cruz, {cross}')
            dom += 1
  return dom

if __name__ == '__main__':
  print('Ejemplos de alcance: ', '\n' )
  example = [[3, 1, 2],
             [4, 5, 2],
             [3, 1, 2]]

  print('En una array tridimencional, como:')

  print('---' * 5)
  for i in example:
    print(*i)
  print('---' * 5)
    
  print(f'Hay {multi_grid(example)} dominante.' , '\n')

  example = [[3, 2, 3],
             [0, 2, 0],
             [3, 2, 3]]

  print('En una array tridimencional, como:')
  
  print('---' * 5)
  for i in example:
    print(*i)
  print('---' * 5)
  
  print(f'Hay {multi_grid(example)} dominantes.', '\n')

  example = [[5, 0, 3, 0, 2],
             [5, 0, 0, 0, 4],
             [5, 0, 3, 0, 2],
             [5, 7, 3, 0, 2],
             [5, 0, 3, 9, 2]]

  print('En una array tridimencional, como:')
  
  print('---' * 5)
  for i in example:
    print(*i)
  print('---' * 5)
  
  print(f'Hay {multi_grid(example)} dominantes.')  
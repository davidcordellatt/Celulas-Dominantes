import random

def bi_grid(grid: list):

  # Autocompletado para evitar errores
  max_len = max([len(col) for col in grid])
  max_num = max([max(col) for col in grid if col !=[]])
  for col in grid:
    if len(col) < max_len:
      while len(col) < max_len:
        col.append(random.randint(1, max_num))
    
        
  
  M = len(grid[0])
  idx = 0
  dom = 0
  while True:
    # Principio
    if idx == 0:
      start = grid[0][0] 
      if start > grid[0][1] and start > grid[1][0] and start > grid[1][1]:
        print(f'Izquierda arriba, {start}')
        dom += 1

      start = grid[1][0]
      if start > grid[0][0] and start > grid[0][1] and start > grid[1][1]:
        print(f'Izquierda abajo, {start}')
        dom += 1
    
    # Final
    if idx == M - 1:
      end = grid[0][-1]
      if end > grid[0][-2] and end > grid[1][-1] and end > grid[1][-2]:
        print(f'Derecha arriba, {end}')
        dom += 1

      end = grid[1][-1]
      if end > grid[1][-2] and end > grid[0][-1] and end > grid[0][-2]:
        print(f'Derecha abajo, {end}')
        dom += 1
    
    # Intermedio
    if idx > 0 and idx < M - 1:
      
      if grid[0][idx] > grid[0][idx - 1] and grid[0][idx] > grid[0][idx + 1] and grid[0][idx] > grid[1][idx + 1] and grid[0][idx] > grid[1][idx] and grid[0][idx] > grid[1][idx - 1]:
        print(f'Top Line, {grid[0][idx]}')
        dom += 1
        
      if grid[1][idx] > grid[1][idx - 1] and grid[1][idx] > grid[1][idx + 1] and grid[1][idx] > grid[0][idx + 1] and grid[1][idx] > grid[0][idx] and grid[1][idx] > grid[0][idx - 1]:
        print(f'Under Line, {grid[1][idx]}')
        dom += 1
      
    idx += 1
    if idx == M:
      break
  return dom

if __name__ == '__main__':
  example = [[0, 0, 2],
             [1, 0, 1]]

  print('En una array bidimencional, como:')

  print('--' * 5)
  for i in example:
    print(*i)
  print('--' * 5)
    
  print(f'Hay {bi_grid(example)} dominantes. El 1 de abajo izquierda, y el 2 de arriba derecha.' , '\n')

  print('\n')

  example = [[0, 2, 0],
             [1, 0, 1]]

  print('En una array bidimencional, como:')
  
  print('--' * 5)
  for i in example:
    print(*i)
  print('--' * 5)
  
  print(f'Hay {bi_grid(example)} dominantes. El 2 de arriba centro' , '\n')

  example = [[0, 0, 3, 0, 0, 0],
             [5, 0, 0, 0, 6, 0]]

  print('En una array bidimencional, como:')
  
  print('--' * 5)
  for i in example:
    print(*i)
  print('--' * 5)
  
  print(f'Hay {bi_grid(example)} dominantes. 5, 3 y 6 en su respectiva posición.')
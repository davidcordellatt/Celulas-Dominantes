from uni_grid import uni_grid
from bi_grid import bi_grid
from multi_grid import multi_grid


N, M = map(int, input().split())

grid = []

for _ in range(N):
  aux = list(map(int, input().split()))
  grid.append(aux)

print(grid)

if N == 1:
  
  print(uni_grid(grid))
  print('---' * 12)
  for col in grid:
    print(*col)
  print('---' * 12)
    
elif N == 2:
  
  print(bi_grid(grid))
  print('---' * 12)
  for col in grid:
    print(*col)
  print('---' * 12)
    
else:
  
  print(multi_grid(grid))
  print('---' * 12)
  for col in grid:
    print(*col)
  print('---' * 12)
def read_input(file):
  grid = []

  with open(file, 'r') as file:
    lines = file.readlines()
    for line in lines:
      grid.append(line)
  return grid

def find_xmas(grid):
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Down-Right
        (-1, -1), # Up-Left
        (1, -1),  # Down-Left
        (-1, 1),  # Up-Right
    ]
    
    word = "XMAS"
    word_length = len(word)
    rows, cols = len(grid), len(grid[0])
    count = 0

    # Helper function to check if the word exists in a given direction
    def check_direction(x, y, dx, dy):
        for i in range(word_length):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < rows and 0 <= ny < cols) or grid[nx][ny] != word[i]:
                return False
        return True

    # Traverse each cell in the grid
    for row in range(rows):
        for col in range(cols):
            for dx, dy in directions:
                if check_direction(row, col, dx, dy):
                    count += 1

    return count

def find_mas(grid):
  Ms = [
      [(-1, -1), (-1, 1)],
      [(-1, 1), (1, 1)],
      [(1, 1), (1, -1)],
      [(-1, -1), (1, -1)]
  ]
  
  Ss = [
     [(1, -1), (1, 1)],
     [(-1, -1), (1, -1)],
     [(-1, -1), (-1, 1)],
     [(-1, 1), (1, 1)]
  ]

  rows, cols = len(grid), len(grid[0])
  count = 0

  def check_diag(x, y, m, s):
      mx1, my1 = x + m[0][0], y + m[0][1]
      mx2, my2 = x + m[1][0], y + m[1][1]
      sx1, sy1 = x + s[0][0], y + s[0][1]
      sx2, sy2 = x + s[1][0], y + s[1][1]

      if not (0 <= mx1 < rows and 0 <= my1 < cols) or \
        not (0 <= mx2 < rows and 0 <= my2 < cols) or \
        not (0 <= sx1 < rows and 0 <= sy1 < cols) or \
        not (0 <= sx2 < rows and 0 <= sy2 < cols):
          return False
      return (grid[mx1][my1] == "M" and grid[mx2][my2] == "M" and grid[sx1][sy1] == "S" and grid[sx2][sy2] == "S")

  for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "A":
              for index in range(len(Ms)):
                if check_diag(row, col, Ms[index], Ss[index]):
                    count += 1
  return count

if __name__ == "__main__":
  grid = read_input('input.txt')
  score = find_mas(grid)
  print(score)
def read_input(file):
  grid = []
  with open(file, 'r') as file:
      for line in file:
          grid.append(list(line.strip()))  # Convert each line into a list of characters
  return grid

# PART 1
def get_start_pos(grid, max_row, max_col):
  for i in range(max_row):
    for j in range(max_col):
      if grid[i][j] == "^":
        return i, j

def next_move(current):
  match current:
    case "^":
      return ">"
    case ">":
      return "v"
    case "v":
      return "<"
    case "<":
      return "^"
    
def out_of_bounds(x, y, max_row, max_col):
  if x > max_row or x < 0:
    return True
  if y > max_col or y < 0:
    return True
  return False

def limit(grid, x, y, move, max_row, max_col):
  if grid[x][y] == "#":
    return False
  if x == max_row and move == "v" or \
    x == 0 and move == "^" or \
    y == max_col and move == ">" or \
    y == 0 and move == "<":
    return True
  return False

def distinct_positions(grid):
  count = 0
  current_move = "^"
  max_row = len(grid) - 1
  max_col = len(grid[0]) - 1
  x, y = get_start_pos(grid, max_row, max_col)
  visited = set()
  while not limit(grid, x, y, current_move, max_row, max_col) and not out_of_bounds(x, y, max_row, max_col):
    if current_move == "^":
      if grid[x][y] == "#":
        current_move = next_move(current_move)
        x += 1
      else:
        if (x, y) not in visited:
          visited.add((x, y))
          count += 1
        x -= 1
    if current_move == ">":
      if grid[x][y] == "#":
        current_move = next_move(current_move)
        y -= 1
      else:
        if (x, y) not in visited:
          visited.add((x, y))
          count += 1
        y += 1
    if current_move == "v":
      if grid[x][y] == "#":
        current_move = next_move(current_move)
        x -= 1
      else:
        if (x, y) not in visited:
          visited.add((x, y))
          count += 1
        x += 1
    if current_move == "<":
      if grid[x][y] == "#":
        current_move = next_move(current_move)
        y += 1
      else:
        if (x, y) not in visited:
          visited.add((x, y))
          count += 1
        y -= 1
  if (x, y) not in visited:
    visited.add((x, y))
    count += 1
  return count

# PART 2


if __name__ == "__main__":
  grid = read_input('input.txt')
  count = distinct_positions(grid)
  print(count)
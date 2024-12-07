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

if __name__ == "__main__":
  grid = read_input('input.txt')
  score = find_xmas(grid)
  print(score)
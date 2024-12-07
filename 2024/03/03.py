import re

def read_input(file):
  rows = []

  with open(file, 'r') as file:
    lines = file.readlines()
    for line in lines:
      rows.append(line)
  return rows

def initiliaze_mul(index1, index2, index3, index4):
  return index1 == "m" and index2 == "u" and index3 == "l" and index4 == "("

def parse_numbers(string):
  pattern = r"\d+"
  numbers = re.findall(pattern, string)
  return int(numbers[0]), int(numbers[1])

def get_muls(rows):
  count = 0
  pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
  
  for row in rows:
    index = 0
    length = len(row)
      
    while index < length - 6:  
      match = re.match(pattern, row[index:])
      if match:
        num1, num2 = map(int, match.groups())
        count += num1 * num2
            
        index += match.end()
      else:
        index += 1

  return count


if __name__ == "__main__":
  rows = read_input('input.txt')
  score = get_muls(rows)
  print(score)
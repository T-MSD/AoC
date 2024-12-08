def read_input(file):
  rules = {}

  with open(file, 'r') as file:
    lines = file.readlines()
    for line in lines:
      num1, num2 = line.strip().split("|")
      rules[int(num1)] = int(num2)
  return rules

if __name__ == "__main__":
  input = read_input('input.txt')
def read_input(file):
  rules = {}
  updates = []

  with open(file, 'r') as file:
    sections = file.read().strip().split("\n\n")
    rule_lines = sections[0].split("\n")
    array_lines = sections[1].split("\n")

    for line in rule_lines:
      num1, num2 = line.split("|")
      rules.setdefault(num1, []).append(num2)

    for line in array_lines:
      updates.append([int(num) for num in line.split(",")])

    return rules, updates

def is_ordered(rules, update):
  
  return True

if __name__ == "__main__":
  rules, updates = read_input('input.txt')
  print(rules)
  print(updates)
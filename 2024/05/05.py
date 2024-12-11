def read_input(file):
  rules = {}
  updates = []

  with open(file, 'r') as file:
    sections = file.read().strip().split("\n\n")
    rule_lines = sections[0].split("\n")
    array_lines = sections[1].split("\n")

    for line in rule_lines:
      num1, num2 = map(int, line.split("|"))
      rules.setdefault(num1, []).append(num2)

    for line in array_lines:
      updates.append([int(num) for num in line.split(",")])

    return rules, updates

def is_ordered(rules, update):
  length = len(update)
  for current_index in range(length):
    current_number = update[current_index]
    for next_number in update[current_index + 1:]:
      if next_number in rules and current_number in rules[next_number]:
        return False
  return True

def middle_number(update):
  index = len(update) // 2
  return update[index]

def page_ordering(rules, updates):
  score = 0
  for update in updates:
    if is_ordered(rules, update):
      score += middle_number(update)
  return score

  

if __name__ == "__main__":
  rules, updates = read_input('input.txt') 
  score = page_ordering(rules, updates)
  print(score)
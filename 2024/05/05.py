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

# Part 1
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

# Part 2
def sort_update(rules, update):
  new_update = []  # This will store the sorted update list.
  remaining_numbers = set(update)  # Set to keep track of remaining numbers in the update.
  # Continue until there are no remaining numbers to place.
  while remaining_numbers:
    for current_number in update:
      if current_number not in remaining_numbers:
        continue
      # Check if current_number can be added to the new_update list (by checking its dependencies in the rules).
      can_insert = True
      for rule in rules.get(current_number, []):
        if rule in remaining_numbers:
          can_insert = False
          break
      if can_insert:
        new_update.append(current_number)  # Add current_number to the sorted list.
        remaining_numbers.remove(current_number)  # Remove from remaining numbers.
        break
  return new_update

def unordered(rules, updates):
  score = 0
  for update in updates:
    if not is_ordered(rules, update):
      ordered_update = sort_update(rules, update)
      score += middle_number(ordered_update)
  return score

if __name__ == "__main__":
  rules, updates = read_input('input.txt') 
  score = unordered(rules, updates)
  print(score)
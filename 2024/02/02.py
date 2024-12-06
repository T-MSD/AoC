def read_file(file):
  reports = []

  with open(file, 'r') as file:
    lines = file.readlines()
    for line in lines:
      numbers = line.split()
      if numbers:
        reports.append([int(x) for x in numbers])
  return reports

def check_adjacent_difference(level1, level2):
  difference = abs(level2 - level1)
  return 1 <= difference <= 3

def is_safe(report):
  length = len(report)
  if report[0] > report[1]:
    for index in range(length - 1):
      if not (report[index] > report[index + 1]) or not check_adjacent_difference(report[index], report[index + 1]):
        return False
    return True
  
  if report[0] < report[1]:
    for index in range(length - 1):
      if not (report[index] < report[index + 1]) or not check_adjacent_difference(report[index], report[index + 1]):
        return False
    return True
  
  return False

def check(list):
  count = 0
  for report in list:
    if is_safe(report):
      count += 1
  return count

def problem_dampener(list):
  count = 0
  for report in list:
    if is_safe(report):
      count += 1
    else:
      length = len(report)
      for index in range(length):
        temp = report[:]
        temp.pop(index)
        if is_safe(temp):
          count += 1
          break
  return count

if __name__ == "__main__":
  input = read_file('input.txt')
  score = problem_dampener(input)
  print(score)

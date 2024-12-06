def read_file(file):
  list1 = []
  list2 = []

  with open(file, 'r') as file:
    lines = file.readlines()
    for line in lines:
      numbers = line.split()
      if numbers:
        list1.append(int(numbers[0]))
        list2.append(int(numbers[1]))

  return list1, list2

def calculate_distance(list1, list2):
  list1.sort()
  list2.sort()
  length = len(list1)
  distance = 0
  for index in range(length):
    distance += abs((list1[index] - list2[index]))
  return distance

def calculate_similarity(list1, list2):
  score = 0
  dict = {}
  for left_number in list1:
    counter = 0
    for right_number in list2:
      if right_number == left_number:
        counter += 1
    if left_number not in dict.keys():
      dict[left_number] = counter
    else:
      dict[left_number] += counter
  for key, value in dict.items():
    score += key * value
  return score

if __name__ == "__main__":
  list1, list2 = read_file('input.txt')
  score = calculate_similarity(list1, list2)
  print(score)
  
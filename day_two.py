def part_one():
  part_one_test()

  file = open("day_two_input.txt", "r")
  input_text = file.read()
  input = input_text.splitlines()
  result = calculate_check_sum(input)

  print("day two part one result: " + str(result))

def part_one_test():
  
  input = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
  result = calculate_check_sum(input)
  if result == 12:
    print("day two part one test passed")
  else:
    print("day two part one test FAILED!" + str(result))


def calculate_check_sum(list_of_boxes):
  twos = 0
  threes = 0
  for box in list_of_boxes:
    if has_exactly_x_copies(box, 2):
      twos += 1
    if has_exactly_x_copies(box, 3):
      threes += 1
  return twos * threes

def has_exactly_x_copies(box_label, x):
  for i in box_label:
    if box_label.count(i) == x:
      return True

  
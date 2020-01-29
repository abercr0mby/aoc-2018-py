def part_two():
  part_two_test()
  file = open("day_two_input.txt", "r")
  input_text = file.read()
  input = input_text.splitlines()
  result = find_correct_boxes(input)

  print("day two part two result: " + str().join(result))
  

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

def part_two_test():
  input = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]

  result = find_correct_boxes(input)
  if result == "fgij":
    print("day two part two test passed")
  else:
    print("day two part two test FAILED!" + str(result))

def find_correct_boxes(boxes):
  diff_index = 0
  for box1 in boxes:
    for box2 in boxes:
      if box1 == box2:
        continue
      diffs = 0
      for index, value in enumerate(box1):
        if value == box2[index]:
          continue
        diffs += 1
        diff_index = index
        if diffs > 1:
          break
      
      if diffs == 1:
        return box1[0:diff_index] + box1[diff_index+1:]
    boxes.remove(box1)


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

  
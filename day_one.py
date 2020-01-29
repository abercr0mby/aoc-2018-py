def day_one_part_two():
  day_one_part_two_test()

  file = open("day_one_input.txt", "r")
  input = file.read()

  result = accumulate_and_collect_until_duplicate(input)
  print("Day one part two result: " + str(result))
  

def day_one_part_one():
  day_one_part_one_test()

  file = open("day_one_input.txt", "r")
  input = file.read()

  result = accumulate_changes(input)
  print("Day one part one result: " + str(result))

def day_one_part_one_test():
  test_input = "+1, +1, +1"
  result = accumulate_changes(test_input)
  if result == 3:
    print("day one part one test one passed")
  else:
    print("day one part one test one FAILED!")

  test_input = "+1, +1, -2"
  result = accumulate_changes(test_input)
  if result == 0:
    print("day one part one test two passed")
  else:
    print("day one part one test two FAILED!")

  test_input = "-1, -2, -3"
  result = accumulate_changes(test_input)
  if result == -6:
    print("day one part one test three passed")
  else:
    print("day one part one test three FAILED!")


def day_one_part_two_test():
  test_input = "+1, -1"
  result = accumulate_and_collect_until_duplicate(test_input)
  if result == 0:
    print("day one part two test one passed")
  else:
    print("day one part two test one FAILED! " + str(result))

  test_input = "+3, +3, +4, -2, -4"
  result = accumulate_and_collect_until_duplicate(test_input)
  if result == 10:
    print("day one part two test two passed")
  else:
    print("day one part two test two FAILED! " + str(result))

  test_input = "-6, +3, +8, +5, -6"
  result = accumulate_and_collect_until_duplicate(test_input)
  if result == 5:
    print("day one part two test three passed")
  else:
    print("day one part two test three FAILED! " + str(result))

  test_input = "+7, +7, -2, -7, -4"
  result = accumulate_and_collect_until_duplicate(test_input)
  if result == 14:
    print("day one part two test four passed")
  else:
    print("day one part two test four FAILED! " + str(result))





def accumulate_and_collect_until_duplicate(input):
  unique_accumulants = {0}
  accumulator = 0

  if input.find(',') > -1:
    changes = [x.strip() for x in input.split(',')]
  else:
    changes = [x.strip() for x in input.splitlines()]

  while True:
    for c in changes:
      if c[0] == '+':
        accumulator += int(c[1:])
      elif c[0] == '-':
        accumulator -= int(c[1:])

      if accumulator in unique_accumulants:
        return accumulator
      else:
        unique_accumulants.add(accumulator)

def accumulate_changes(input):
  accumulator = 0
  if input.find(',') > -1:
    changes = [x.strip() for x in input.split(',')]
  else:
    changes = [x.strip() for x in input.splitlines()]
  
  for c in changes:
    if c[0] == '+':
      accumulator += int(c[1:])
    elif c[0] == '-':
      accumulator -= int(c[1:])

  return accumulator
    
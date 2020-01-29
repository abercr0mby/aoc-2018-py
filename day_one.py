def day_one():
  day_one_part_one_test()

  file = open("day_one_part_one_input.txt", "r")
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

def accumulate_changes(input):
  accumulator = 0
  if input.find(',') > -1:
    changes = [x.strip() for x in input.split(',')]
  else:
    changes = [x.strip() for x in input.splitlines()]
  
  print (len(changes))
  print (changes[0])

  for c in changes:
    if c[0] == '+':
      accumulator += int(c[1:])
    elif c[0] == '-':
      accumulator -= int(c[1:])

  return accumulator
    
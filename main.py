"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.


def foo(x):

  if x <= 1:
    return x
  ra = foo(x - 1)
  rb = foo(x - 2)

  return ra + rb


def longest_run(mylist, key):

  runNums = []
  runNum = 0

  for i in range(len(mylist)):
    if mylist[i] == key:
      runNum += 1
    else:
      runNums.append(runNum)
      runNum = 0
    runNums.append(runNum)

  longRun = max(runNums)

  return longRun


class Result:
  """ done """

  def __init__(self, left_size, right_size, longest_size, is_entire_range):
    self.left_size = left_size  # run on left side of input
    self.right_size = right_size  # run on right side of input
    self.longest_size = longest_size  # longest run in input
    self.is_entire_range = is_entire_range  # True if the entire input matches the key

  def __repr__(self):
    return ('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
            (self.longest_size, self.left_size, self.right_size,
             self.is_entire_range))


def longest_run_recursive(mylist, key):

  if len(mylist) == 0:
    return Result(0, 0, 0, False)
  if len(mylist) == 1 and mylist[0] == key:
    return Result(1, 1, 1, True)
  elif len(mylist) == 1 and mylist[0] != key:
    return Result(0, 0, 0, False)

  return merge(longest_run_recursive(mylist[len(mylist) // 2:], key),
               longest_run_recursive(mylist[:len(mylist) // 2], key))


def merge(a, b):

  ier = False

  middle_size=a.right_size+b.left_size

  left_size = a.left_size
  if a.is_entire_range:
    left_size = a.longest_size+b.left_size
    middle_size=a.longest_size+b.left_size

  right_size = b.right_size
  if b.is_entire_range:
    right_size = b.longest_size+a.right_size
    middle_size=b.longest_size+a.right_size
    

  longest = max(left_size, right_size, middle_size,a.longest_size,b.longest_size)

  if a.is_entire_range and b.is_entire_range:
    longest = a.longest_size + b.longest_size
    ier = True

  return Result(left_size, right_size, longest, ier)


def merge2(a, b):

  ier = False
  left_size = 0
  right_size = 0
  longest = 0

  return Result(left_size, right_size, longest, ier)


## Feel free to add your own tests here.
def test_longest_run():
  assert longest_run([2, 12, 12, 8, 12, 12, 12, 0, 12, 1], 12) == 3


def tests():

  a = Result(0, 0, 0, False)
  assert type(a) == Result

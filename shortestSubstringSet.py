def shortestSubstringSet(s, set):
  minLen = 0
  for i range(len(s)-len(set)):
    seen = []
    for j in range(len(set), len(s))
      length, seen = checkControlsSet(s[i:j], set, seen)
      minLen = min(length, minLen)
  return minLen

def checkControlsSet(subString, set, seen):
  d = {}
  for char in set:
    d[char] = 0
  for char in seen:
    d[char] = 1

  for i in len(subString):
    if subString[i] in d.keys():
      d[subString[i]] = 1
  for val in d.values:
    if val != 1:
      return -1
  return len(subString)




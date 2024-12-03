import re

with open("puzzle.txt", "r") as file:
    data = file.read()

# found with https://regexr.com/
pattern = r"mul\((\d+),(\d+)\)"

matches = re.findall(pattern, data)

total_sum = 0
for (x,y) in matches:
    total_sum += int(x) * int(y)

print(total_sum)

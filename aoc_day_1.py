import re

word_to_num = {
    "oneight": 18,
    "twone": 21,
    "threeight": 38,
    "nineight": 98,
    "fiveight": 58,
    "sevenine": 79,
    "eightwo": 82,
    "eighthree": 83,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
f = open("/Users/michaeljohnson/Downloads/input.txt", "r")
q1_numbers = []
q2_numbers = []
for line in f:
    nums = re.findall("[0-9]+", line)
    num = ""
    for s in nums:
        num += s
    q1_numbers.append(int(f"{num[0]}{num[-1]}"))
    for key, item in word_to_num.items():
        line = line.replace(key, str(item))
    _nums = re.findall("[0-9]+", line)
    num = ""
    for s in _nums:
        num += s
    q2_numbers.append(int(f"{num[0]}{num[-1]}"))


print(sum(q1_numbers))
print(sum(q2_numbers))

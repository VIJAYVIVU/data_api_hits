items = list(range(1000000))
# This has to check every item until it finds 999999
if 999999 in items:
    print("Found!")

words = ["Python", "is", "great", "for", "data"]
sentence = ""
for word in words:
    sentence += word + " "  # Creates a new string object every iteration
print(sentence)


numbers = [1, 2, 3, 4, 5]
squared = []
for n in numbers:
    squared.append(n * n)


import math

def calculate():
    result = []
    for i in range(1000000):
        # Python looks up 'math' and 'sin' in the global scope every time
        result.append(math.sin(i))

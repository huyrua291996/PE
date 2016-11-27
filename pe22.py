def name_score(name):
    score = 0
    for char in name:
        score += ord(char) - ord('A') + 1
    return score


with open("names.txt", "r") as f:
    names = f.read()
    names = names.replace('"', '')
    names = names.split(',')
    names.sort()
sum_ = 0
for name in range(len(names)):
    score = name_score(names[name]) * (name + 1)
    sum_ += score
print(sum_)
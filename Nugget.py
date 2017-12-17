package = (6, 9, 20)
candidate = package[0]
consecutivecount = 0
def possiblenuggets(number):
    obtainable = None
    for i in range(15):
        for j in range(15):
            for k in range(15):
                check = package[0] * i + package[1] * j + package[2] * k
                if check == number:
                    obtainable = check
    if obtainable:
        return True
    else:
        return False

while(consecutivecount != package[0]):
    if(possiblenuggets(candidate)):
        consecutivecount += 1
    else:
        largest = candidate
        consecutivecount = 0
    candidate += 1

print(largest)

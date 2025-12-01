current = 50
zeroCount = 0

def rotateRight(current, clicksToRotate):
    value = (current + clicksToRotate) % 100
    return  value


def rotateLeft(current, clicksToRotate):
    value = (current - clicksToRotate) % 100
    return value + 100 if value < 0 else value

with open("inputs/day1.txt") as f:
    for line in f:
        line = line.strip()
        direction = line[0:1].strip()
        clicks = int(line[1:].strip())

        if direction == "L":
            current = rotateLeft(current, clicks)
        if direction == "R":
            current = rotateRight(current, clicks)
        if current == 0:
            zeroCount = zeroCount + 1

        print( current )

print("------------")
print(zeroCount)
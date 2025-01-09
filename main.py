def hittable_targets(room):
    # Your implementation here!
    count = 0

    row = -1
    column = -1


    for i in range(len(room)):
        for j in range(len(room[i])):
            if room[i][j] == "A":
                row = i
                column = j

    for i in reversed(range(0, column)):
        if room[row][i] == "T":
            count += 1
            break
        elif room[row][i] == "W":
            break

    for i in range(column, len(room[0])):
        if room[row][i] == "T":
            count += 1
            break
        elif room[row][i] == "W":
            break
    
    for i in reversed(range(0, row)):
        if room[i][column] == "T":
            count += 1
            break
        elif room[i][column] == "W":
            break
    
    for i in range(row, len(room)):
        if room[i][column] == "T":
            count += 1
            break
        elif room[i][column] == "W":
            break

    return count
    


room1 = [
    [' ', 'T', 'W', ' ', 'T'],
    ['T', ' ', ' ', ' ', ' '],
    [' ', 'A', ' ', 'T', 'T'],
    [' ', ' ', ' ', ' ', ' '],
    ['W', 'W', 'W', ' ', ' '],
    [' ', 'T', ' ', ' ', ' '],
]

assert hittable_targets(room1) == 2

room2 = [
    [' ', 'T', ' ', ' '],
    ['T', 'A', 'T', ' '],
    [' ', 'T', ' ', ' '],
]
assert hittable_targets(room2) == 4

room3 = [
    ['T', ' ', 'T'],
    [' ', 'A', ' '],
    ['T', ' ', 'T'],
    [' ', ' ', ' '],
]
assert hittable_targets(room3) == 0

room4 = [
    ['T', 'A', ' ', 'W', ' ', 'T'],
]
assert hittable_targets(room4) == 1

room5 = [
    ['A'],
]
assert hittable_targets(room5) == 0

print("All tests passed!")
print("If time remains, discuss time & space complexity")

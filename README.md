# slingshot-problem
Problem to be completed during Industry Prep - Interview Prep activity time

## Problem Statement

Auberon has a slingshot and they are using it to shoot targets. The room Auberon is in is represented by a rectangular 2D list of strings where:

'A' represents where Auberon is standing.
'T' is a target.
'W' is a wall.
' ' is an empty space.

For example:
```py
[
    [' ', 'T', 'W', ' ', 'T'],
    ['T', ' ', ' ', ' ', ' '],
    [' ', 'A', ' ', 'T', 'T'],
    [' ', ' ', ' ', ' ', ' '],
    ['W', 'W', 'W', ' ', ' '],
    [' ', 'T', ' ', ' ', ' '],
]
```

Auberon is only able to shoot their slingshot up, down, left, or right. They cannot shoot at a diagonal.

Their pellet travels until it either hits a target, a wall, or exits the room. The pellet cannot pass through walls or targets.

In this example, Auberon is able to hit two targets: one above them (row 0, column 1), and one to the right of them (row 2, column 3).

Write a function that takes in a 2D list of strings representing a room and returns the number of targets Auberon is able to hit.

## Examples

### Example 1
```py
room1 = [
    [' ', 'T', 'W', ' ', 'T'],
    ['T', ' ', ' ', ' ', ' '],
    [' ', 'A', ' ', 'T', 'T'],
    [' ', ' ', ' ', ' ', ' '],
    ['W', 'W', 'W', ' ', ' '],
    [' ', 'T', ' ', ' ', ' '],
]

hittable_targets(room1)
```
Produces
```py
2
```

### Example 2
```py
room2 = [
    [' ', 'T', ' ', ' '],
    ['T', 'A', 'T', ' '],
    [' ', 'T', ' ', ' '],
]

hittable_targets(room2)
```
Produces
```py
4
```

### Example 3
```py
room3 = [
    ['T', ' ', 'T'],
    [' ', 'A', ' '],
    ['T', ' ', 'T'],
    [' ', ' ', ' '],
]

hittable_targets(room3)
```
Produces
```py
0
```

### Example 4
```py
room4 = [
    ['T', 'A', ' ', 'W', ' ', 'T'],
]

hittable_targets(room4)
```
Produces
```py
1
```

### Example 5
```py
room5 = [
    ['A'],
]

hittable_targets(room5)
```
Produces
```py
0
```

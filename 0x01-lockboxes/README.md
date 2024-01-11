# Lockboxes

## Overview

This project, part of ALX Africa Intranet's Algorithm curriculum, focuses on solving the Lockboxes problem using Python. The task involves determining if a given set of locked boxes can all be opened. Each box is numbered from 0 to n - 1 and may contain keys to other boxes.

## Task

### 0. Lockboxes (mandatory)

- Implement a Python method `def canUnlockAll(boxes)` that determines if all the locked boxes can be opened. The boxes are represented as a list of lists, where a key with the same number as a box opens that box. The first box `boxes[0]` is unlocked. Return `True` if all boxes can be opened, else return `False`.

## Test Script

```bash
$ cat main_0.py
#!/usr/bin/python3
canUnlockAll = __import__('0-lockboxes').canUnlockAll
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False.
```


## How to Run

Execute `./0-main.py` to test your `canUnlockAll` function.

## Support

For issues or help, contact for assistance.

## Copyright

Copyright © 2024 ALX. All rights reserved.

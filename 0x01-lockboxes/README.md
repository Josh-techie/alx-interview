<p align="center">
<img src ="https://media.istockphoto.com/id/1194118007/photo/half-opened-silver-steel-post-office-box-with-keys-inside-the-lock.jpg?s=612x612&w=0&k=20&c=LHMt_ZFGcVXLle73y38h-lm4KB2qCtQtNG9wZxs98Xw=">
</p>

---

# Lockboxes

## Overview

This project, part of ALX Africa Intranet's Algorithm curriculum, focuses on solving the Lockboxes problem using Python. The task involves determining if a given set of locked boxes can all be opened. Each box is numbered from 0 to n - 1 and may contain keys to other boxes.

---

## Task

- Implement a Python method `def canUnlockAll(boxes)` that determines if all the locked boxes can be opened. The boxes are represented as a list of lists, where a key with the same number as a box opens that box. The first box `boxes[0]` is unlocked. Return `True` if all boxes can be opened, else return `False`.

---

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

---

## How to Run

Execute `./0-main.py` to test your `canUnlockAll` function.

---

## Author

- [`@Josh-techie`]() | Software Engineer Student

  > Reach out to me if you need any help or have any questions.

  <a href="mailto:youssef.abouyahia@e-polytechnique.ma">
  	<img alt="Feel free to contact me" src="https://img.shields.io/badge/-Ask_me_anything-blue?style=flat&logo=Gmail&logoColor=white&link=mailto:youssef.abouyahia@e-polytechnique.ma&color=3d85c6" />
  </a>
  <span> | </span>
    <a href="https://www.linkedin.com/in/youssef-abouyahia/">
        <img alt="Linkedin Profile" src="https://img.shields.io/badge/-Linkedin-0072b1?style=flat&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/youssef-abouyahia/" />
    </a>
    <span> | </span>
    <a href="https://twitter.com/JoesephAb">
        <img alt="Twitter Profile" src="https://img.shields.io/badge/-Twitter-0072b1?style=flat&logo=Twitter&logoColor=white&link=https://twitter.com/JoesephAb&color=1DA1F2" />
    </a>

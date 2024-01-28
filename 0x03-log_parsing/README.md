<p align="center">
<img src ="https://fedingo.com/wp-content/uploads/2021/07/extract-ip-address.jpg">
</p>

---

# Log Parsing

## Overview

This project, part of [ALX Africa](https://www.alxafrica.com/) Intranet's Algorithm curriculum, involves creating a Python script for log parsing. The script reads input from standard input (stdin) line by line, processes the data, and computes various metrics. The goal is to print statistics after every 10 lines or when interrupted with CTRL + C.

---

## Project Structure

- **Directory:** 0x03-log_parsing
- **File:** [0-stats.py](./0-stats.py)

## Tasks

 **0. Log parsing**:

- Write a script that reads stdin line by line and computes metrics based on the given input format.
- Metrics include total file size and number of lines by status code.
- Status codes: 200, 301, 400, 401, 403, 404, 405, and 500.

---

## Test Script

```bash
$ cat 0-generator.py
#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

# (Generator script details...)

$ ./0-generator.py | ./0-stats.py
# Example output after a few iterations...
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
```

---

## How to Run

Execute `./0-generator.py | ./0-stats.py` to test the log parsing script.

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

<p align="center">
<img src ="https://coderscat.com/images/island.png">
</p>

---

<h2> Making Change </h2>

- In the **Island Perimeter** project, the task is to create a Python function that calculates the perimeter of a single island within a 2D grid. The grid consists of water (0) and land (1), and the goal is to apply logical operations to identify land cells and determine their contribution to the island's perimeter. The project emphasizes the use of 2D arrays, conditional logic, and problem-solving strategies. The code must adhere to PEP 8 style guidelines, be executable on Ubuntu 20.04 LTS using Python 3.4.3, and include documentation for all modules and functions. This project provides an opportunity to reinforce algorithmic thinking and data structure manipulation skills in a Python context.

---

<h2> Resources </h2>

- [Nested Lists](https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions)
- [Python Multi-dimensional Arrays](https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/)
- [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)
- [Python 2D arrays and lists](https://www.youtube.com/watch?v=aNzepGawwCI)

> Additional Resources

- [Mock Technical Interview](https://www.youtube.com/watch?v=fFgEM6CMQc4)

---

---

<h2> Repository Structure </h2>

- **Directory:** 0x09-island_perimeter
- **File:** [0-island_perimeter.py](./0-island_perimeter.py)

---

<h2> Steps to Follow </h2>

1- **Create the Python File** : Start by creating a new Python file named `0-island_perimeter.py` for your island perimeter calculation function.

2- **Implement the Island Perimeter Function** : Open `0-island_perimeter.py` and implement the function `island_perimeter(grid)` as per the project specifications. Utilize concepts such as 2D arrays, conditional logic, and problem-solving strategies.

3- **Run the Test Script** : Execute the provided test script `0-main.py` to verify the correctness of your `island_perimeter` function.

4- **Check the Output** : Examine the output of your script to ensure that it matches the expected results for the given test cases.

```bash
#!/usr/bin/python3
""" Main file for testing """

island_perimeter = __import__('0-island_perimeter').island_perimeter

grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

print(island_perimeter(grid))  # Output Should be: 12
```

---

<h2> Author </h2>

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

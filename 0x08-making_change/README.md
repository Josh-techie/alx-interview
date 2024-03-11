<p align="center">
<img src ="https://th.bing.com/th/id/R.d0240a4a89adb1ad99b956940bff5129?rik=35IVEpcAs6sk6w&riu=http%3a%2f%2fwww.csharpstar.com%2fwp-content%2fuploads%2f2017%2f03%2fCoin_changing.jpg&ehk=ssNG8kCvQRRcqS0L1n%2fs9PP0Kufuw3w4%2fSQqseqVL%2bQ%3d&risl=&pid=ImgRaw&r=0">
</p>

---

<h2> Making Change </h2>

- <p> In this project, I am tasked with solving the classic coin change problem using dynamic programming and greedy algorithms. The goal is to determine the fewest number of coins needed to meet a given total amount, considering a pile of coins with different values. I need to carefully choose between a greedy algorithm and a dynamic programming approach based on the specific coin denominations provided. The project tests my algorithmic skills, understanding of overlapping subproblems, and the ability to analyze time and space complexity. The implementation is required to adhere to PEP 8 style guidelines and pass runtime evaluations. This project is an opportunity to strengthen my problem-solving and Python programming skills within the context of algorithmic challenges. </p>

---

<h2> Resources </h2>

- [More Control Flow Tools (for loops, if statements)](https://docs.python.org/3/tutorial/controlflow.html)
- [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
- [Greedy Algorithm to find Minimum number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)
- [Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=jgiZlGzXMBw)

> Additional Resources

- [Mock Technical Interview](https://intranet.alxswe.com/rltoken/ktLaKIVRkq_-byFO-_-aGg)

---

<h2> Task </h2>

- **Island Perimeter:**
  - Implement the function `island_perimeter(grid)` to calculate the perimeter of the island described in the given 2D grid.
  - Prototype: `def island_perimeter(grid) -> int`.
  - The input `grid` is a list of lists of integers, where:
    - 0 represents water.
    - 1 represents land.
    - Each cell is a square with a side length of 1.
    - Cells are connected horizontally/vertically (not diagonally).
    - The grid is rectangular, with its width and height not exceeding 100.
    - The grid is completely surrounded by water.
    - There is only one island (or nothing), and the island doesn't have "lakes" (water inside that isn't connected to the water surrounding the island).
  - Apply concepts of 2D arrays, conditional logic, and counting techniques to identify and calculate the perimeter of the island.
  - Use nested loops for iterating over grid cells and conditional statements to check the status of adjacent cells.
  - Adhere to PEP 8 style guidelines (version 1.7).
  - Ensure all modules and functions are documented.
  - Make all files executable.
  - Test your implementation using the provided test script `0-main.py` and verify that the output matches the expected results.

---

<h2> Repository Structure </h2>

- **Directory:** 0x08-making_change
- **File:** [0-making_change.py](/0-making_change.py)

---

<h2> Steps to Follow </h2>

1- **Create the Python File** : Create a new Python file for your coin change algorithm and name it `0-making_change.py`.

2- **Implement the Coin Change Function** : Open `0-making_change.py` and implement the function `makeChange(coins, total)` according to the project requirements.

3- **Run the Script** : Run your `0-main.py` script to test the functionality of your `makeChange` function.

4- **Test Script** : Test your script by using the provided test cases in `0-main.py` and check if the output matches the expected results.

```bash
#!/usr/bin/python3
""" Main file for testing """

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))  # Output Should be: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output Should be: -1
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

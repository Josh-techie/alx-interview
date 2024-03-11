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

- Making Change:
  - Implement the function `makeChange(coins, total)` to find the fewest number of coins needed to meet a given total amount.
  - Prototype: `def makeChange(coins, total)`.
  - Return the fewest number of coins needed to meet the total.
  - If the total is 0 or less, return 0.
  - If the total cannot be met by any number of coins, return -1.
  - The input `coins` is a list of values representing the denominations of coins.
  - The value of a coin will always be an integer greater than 0.
  - Assume an infinite number of each denomination of coin in the list.
  - The solution's runtime will be evaluated.

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

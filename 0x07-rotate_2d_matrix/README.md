<p align="center">
<img src ="https://www.codespeedy.com/wp-content/uploads/2018/12/rotate-1.jpg">
</p>

---

<h2> Rotate 2D Matrix </h2>

- This project focuses on implementing an in-place algorithm in Python to rotate an n x n 2D matrix by 90 degrees clockwise. The task requires a solid understanding of matrix manipulation, in-place operations, and optimization for space complexity. The goal is to efficiently rotate the matrix by transposing it and reversing each row. The project encourages participants to enhance their problem-solving and algorithmic thinking skills within the specified deadline.

---

<h2> Ressources </h2>

- [Data Structures (list comprehensions, nested list comprehension)](https://docs.python.org/3/tutorial/datastructures.html)
- [Inplace rotate square matrix by 90 degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
- [Transpose a matrix in Single line in Python](https://www.geeksforgeeks.org/transpose-matrix-single-line-python/)
- [Python - Lists](https://www.tutorialspoint.com/python/python_lists.htm)
- [Mock-Interview](https://www.youtube.com/watch?v=yM9Xbi-MigE)

---

<h2> Task </h2>

- Rotate 2D Matrix :
  - Given an n x n 2D matrix, your task is to rotate it 90 degrees clockwise.
  - Prototype: def rotate_2d_matrix(matrix):
  - Do not return anything. Edit the matrix in-place.
  - You can assume the matrix will have 2 dimensions and will not be empty.

---

<h2> Repository Structure </h2>

- **Directory:** 0x07-rotate_2d_matrix
- **File:** [0-rotate_2d_matrix.py](/0-rotate_2d_matrix.py)

---

<h2> Steps to Follow </h2>

1- **Create the Python File** : Create a new Python file for your 2D matrix, rotation and name it `0-rotate_2d_matrix.py`.

2- **Implement the 2D Matrice Function** : Open `0-rotate_2d_matrix.py` and the function `rotate_2d_matrix` in your script.

3- **Run the Script** : Run your `main_0.py` script to see the magic happen

4- **Test Script** : Test your script by feeding it these inputs and check the output of it checks, what's listed below.

```bash
#!/usr/bin/python3
""" Test 0x07 - Rotate 2D Matrix """

rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate_2d_matrix(matrix)
    print(matrix)
```

> Output Should be: `[[7, 4, 1], [8, 5, 2], [9, 6, 3]]`

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

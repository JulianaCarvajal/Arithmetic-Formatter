# Arithmetic-Formatter

This is a Python project that formats arithmetic problems provided as strings in a visually appealing way. It is part of the Scientific Computing with Python Certification, by freeCodeCamp.

## Installing 

To use this project, you should have Python 3 installed. Clone or download the repository, and navigate to the project directory on your terminal/command prompt.

```bash
git clone https://github.com/JulianaCarvajal/Arithmetic-Formatter.git
cd Arithmetic-Formatter
```

## Usage

The project includes the following files:

- `arithmetic_arranger.py`: This is the main file that includes the `arithmetic_arranger()` function that formats the arithmetic problems.

- `main.py`: This file includes an example of how to use the `arithmetic_arranger()` function.

- `test_module.py`: This file includes several tests for the `arithmetic_arranger()` function.

To format arithmetic problems, you can use the `arithmetic_arranger()` function in the `arithmetic_arranger.py` file. The function accepts two arguments: a list of arithmetic problems as strings and a Boolean value indicating whether to show the answers. The function returns a formatted string with the arithmetic problems arranged vertically.

Here is an example of how to use the `arithmetic_arranger()` function:

```python
from arithmetic_arranger import arithmetic_arranger

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems))
```

The output of the code above will be:

```text
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

To run the tests, you can use the `test_module.py` file:

```bash
python test_module.py
```
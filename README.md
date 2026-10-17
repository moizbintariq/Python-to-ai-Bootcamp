# Python Practice

Practice work from the Python to AI Bootcamp (Day 1 and Day 2).

## Structure
```
python-practice/
├── README.md
├── day1/
│   ├── 01_variables_and_types.py
│   ├── 02_operators.py
│   ├── 03_conditions.py
│   ├── 04_loops.py
│   ├── 05_strings.py
│   ├── 06_lists_tuples_sets.py
│   ├── 07_dictionaries.py
│   ├── 08_functions.py
│   └── 09_marks_analyzer.py
└── day2/
    ├── titanic.csv
    ├── numpy_basics.ipynb
    └── titanic_analysis.ipynb
```

## Day 1: Python fundamentals
Variables and types, type conversion, operators, `if / elif / else`, `for` and `while` loops, `break` and `continue`, strings, lists, tuples, sets, dictionaries and functions.
`09_marks_analyzer.py` is a mini project that also shows the highest and lowest marks using `max()` and `min()`.

## Day 2: NumPy and Pandas
- `numpy_basics.ipynb`: arrays, `sum`, `mean`, `max`, `min`
- `titanic_analysis.ipynb`: `read_csv`, `head`, `tail`, `shape`, `info`, `describe`, `isnull().sum()`, `loc`, `iloc`, `value_counts`, plus my own questions:
  1. Girls under 18 in 3rd class who survived
  2. Passengers travelling alone in 2nd class who survived
  3. Children (under 10) compared with adults
  4. Passengers who paid a fare above 100
  5. Bonus: average fare at each port

## How to run
```bash
pip install pandas numpy jupyter
python day1/04_loops.py
jupyter notebook
```

# Pizza Py

Perhaps the most popular place for pizza in Harvard Square is Pinocchio’s Pizza & Subs, aka Noch’s, known for its Sicilian pizza, which is “a deep-dish or thick-crust pizza.”

Students tend to buy pizza by the slice, but Pinocchio’s also has whole pizzas on its menu too, per this CSV file of Sicilian pizzas, [sicilian.csv](sicilian.csv), below:

    Sicilian Pizza,Small,Large
    Cheese,$25.50,$39.95
    1 item,$27.50,$41.95
    2 items,$29.50,$43.95
    3 items,$31.50,$45.95
    Special,$33.50,$47.95

See [regular.csv](regular.csv) for a CSV file of regular pizzas as well.

Of course, a CSV file isn’t the most customer-friendly format to look at. Prettier might be a table, formatted as ASCII art, like this one:
```shell
    +------------------+---------+---------+
    | Sicilian Pizza   | Small   | Large   |
    +==================+=========+=========+
    | Cheese           | $25.50  | $39.95  |
    +------------------+---------+---------+
    | 1 item           | $27.50  | $41.95  |
    +------------------+---------+---------+
    | 2 items          | $29.50  | $43.95  |
    +------------------+---------+---------+
    | 3 items          | $31.50  | $45.95  |
    +------------------+---------+---------+
    | Special          | $33.50  | $47.95  |
    +------------------+---------+---------+
```
In a file called `pizza.py`, implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using `tabulate`, a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s `grid` format. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in `.csv`, or if the specified file does not exist, the program should instead exit via `sys.exit`.


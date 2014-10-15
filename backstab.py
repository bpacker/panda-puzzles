__author__ = 'ben.packer'

from constraint import *

# According to the puzzle, the max stabbings should be 30, but set this lower to reduce CPU and memory usage
MAX_STABBINGS = 6

# Abbreviate so they each fit within a tab
names = ["Lady M", "Titania", "Gert", "Goneril", "Ros", "Des"]

# For convenience, label the rows a-f and the columns 0-6
rows = ["a", "b", "c", "d", "e", "f"]
columns = range(0, 6)


def var_name(row, column):
    return row + str(column)


def print_solution(solution):
    col_str = "\t"
    for name in names:
        col_str += "%s\t" % name
    print col_str
    for idx, row in enumerate(rows):
        row_str = "%s\t" % names[idx]
        for column in columns:
            row_str += "%s\t" % str(solution[var_name(row, column)])
        print row_str


problem = Problem()
for row in rows:
    for column in columns:
        # Rule 1
        if row == "a" and column > 0:
            problem.addVariable(var_name(row, column), range(5, 31, 5))
        else:
            problem.addVariable(var_name(row, column), range(0, MAX_STABBINGS + 1))

for idx1, row in enumerate(rows):
    for idx2, column in enumerate(columns):
        if idx1 == idx2:
            # Rule 2
            problem.addConstraint(lambda x: x == 0, [var_name(row, column)])
        else:
            # Rule 3
            problem.addConstraint(lambda x: x > 0, [var_name(row, column)])

# Rule 4
problem.addConstraint(AllEqualConstraint(), ["a1", "a2", "a3", "a4", "a5"])
problem.addConstraint(AllEqualConstraint(), ["f0", "f1", "f2", "f3", "f4"])
problem.addConstraint(lambda x, y: x == 5*y, ("a1", "f1"))
for row in rows[1:]:
    for column in columns:
        problem.addConstraint(lambda x, y: x > y, ("a1", var_name(row, column)))

# Rule 5
problem.addConstraint(SomeInSetConstraint([3]), ["d1", "d2", "d4", "d5"])
problem.addConstraint(lambda x: x != 3, ["d0"])
problem.addConstraint(SomeInSetConstraint([3]), ["b0", "c0", "d0", "e0", "f0"])

# Rule 6
problem.addConstraint(SomeInSetConstraint([3]), ["e0", "e1", "e2", "e3", "e5"])

# Rule 7
problem.addConstraint(SomeInSetConstraint([1]), ["a5", "b5", "c5", "e5"])
problem.addConstraint(lambda x: x != 1, ["d5"])

# Rule 8
problem.addConstraint(AllEqualConstraint(), ["c1", "d1", "e1", "f1"])

# Rule 9
problem.addConstraint(lambda x, y: x + y >= 7, ("b5", "d0"))

# Rule 10
problem.addConstraint(lambda x, y: x == y * 2, ("d2", "d4"))

# Rule 11
problem.addConstraint(AllEqualConstraint(), ["b3", "c3", "e3"])
for var in ["b3", "c3", "e3"]:
    problem.addConstraint(lambda x: x >= 4, [var])

# Rule 12
problem.addConstraint(lambda a, b, c, d, e: [a, b, c, d, e].count(2) >= 2, ("b0", "c0", "d0", "e0", "f0"))
#problem.addConstraint(SomeInSetConstraint([2]), ["b0", "c0", "d0", "e0", "f0"])

# Rule 13
problem.addConstraint(lambda x, y: x + y in [4, 9, 16, 25, 36, 49], ("e0", "a4"))

# Rule 14
problem.addConstraint(AllDifferentConstraint(), ["a4", "b4", "c4", "d4", "f4"])

# Rule 15
for var in ["c0", "c1", "c3", "c4", "c5"]:
    problem.addConstraint(lambda x: x % 2 == 1, [var])

# Rule 16
#problem.addConstraint(SomeInSetConstraint([4]), ["a2", "b2", "d2", "e2", "f2"])
problem.addConstraint(lambda a, b, c, d, e: [a, b, c, d, e].count(4) >= 2, ("a2", "b2", "d2", "e2", "f2"))

# Rule 17
problem.addConstraint(lambda x, y: x == y, ("b4", "e5"))

solutions = problem.getSolutions()
print "Number of solutions: %d" % len(solutions)

print_solution(solutions[0])
print_solution(solutions[-1])
"""
multiplication-table.py
Author: Meg
Credit: https://stackoverflow.com/questions/3249524/print-in-one-line-dynamically (How to keep on one line)
https://stackoverflow.com/questions/38475578/how-to-format-output-to-create-space-between-two-variables-in-python-when-printi(format)
Assignment:

Write and submit a Python program that prints a multiplication table. The user 
must be prompted to give the width and height of the table before it is printed.

The final multiplication table should look like this:

Width of multiplication table: 10
Height of multiplication table: 8

  1   2   3   4   5   6   7   8   9  10
  2   4   6   8  10  12  14  16  18  20
  3   6   9  12  15  18  21  24  27  30
  4   8  12  16  20  24  28  32  36  40
  5  10  15  20  25  30  35  40  45  50
  6  12  18  24  30  36  42  48  54  60
  7  14  21  28  35  42  49  56  63  70
  8  16  24  32  40  48  56  64  72  80
"""
column = int(input("Width of multiplication table: "))
row = int(input("Height of multiplication table: "))
print()

width=
i = 1
a = 1
for i in range(1, column):
    print('{0:{width}{i}}'.format(i, width=width, i=i),end=' ')
    i+=1
print(i)
i=1
for i in range(1, row):
    print(i+1, end=" ")
    for i in range(1, column-1):
        print((i+1)*(a+1),end=" ")
        i+=1
    print((i+1)*(a+1))
    i+=1
    a+=1
## add
Assigned from Mixed Level on 03/03/2020
Hey! ✨

I'd like you to write a function that accepts two lists-of-lists of numbers and returns one list-of-lists with each of the corresponding numbers in the two given lists-of-lists added together.

It should work something like this:

```
matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]
add(matrix1, matrix2)
[[3, -3], [-3, 3]]
matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
add(matrix1, matrix2)
[[2, -1, 3], [-3, 3, -3], [5, -6, 7]]
```

Try to solve this exercise without using any third-party libraries (without using pandas for example).

Before attempting any bonuses, I'd like you to put some effort into figuring out the clearest and most idiomatic way to solve this problem. If you're using indexes to loop, take a look at the first hint.

There are two bonuses this week.

## Bonus 1

For the first bonus, modify your add function to accept and "add" any number of lists-of-lists. ✔️

```
matrix1 = [[1, 9], [7, 3]]
matrix2 = [[5, -4], [3, 3]]
matrix3 = [[2, 3], [-3, 1]]
add(matrix1, matrix2, matrix3)
[[8, 8], [7, 7]]
```

## Bonus 2

For the second bonus, make sure your add function raises a ValueError if the given lists-of-lists aren't all the same shape. ✔️
```
add([[1, 9], [7, 3]], [[1, 2], [3]])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "add.py", line 10, in add
    raise ValueError("Given matrices are not the same size.")
ValueError: Given matrices are not the same size.
```
## Hints

Hints for when you get stuck (hover over links to see what they're about):


Iterating lists with and without indexes
Multiple assignment might come in handy
A special syntax for creating new lists from old lists
Accepting any number of arguments to a function
More discussion on accepting any number of arguments
Raising an exception in Python

<ul>
<li><a href="http://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/" title="When looping over multiple lists at once, indexes aren't usually necessary">Iterating lists with and without indexes</a></li>
<li><a href="https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/" title="Multiple assignment is very common to see while looping">Multiple assignment might come in handy</a></li>
<li><a href="https://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/" title="List comprehensions are a special purpose tool for a special kind of looping">A special syntax for creating new lists from old lists</a></li>
<li><a href="https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/#Asterisks_for_packing_arguments_given_to_function" title="*args and **kwargs idiom allows accepting multiple arguments passed to a function">Accepting any number of arguments to a function</a></li>
<li><a href="https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters/36908#36908" title="Lots of examples of * and ** in here">More discussion on accepting any number of arguments</a></li>
<li><a href="https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python" title="Examples of how to raise an manually exception in Python">Raising an exception in Python</a></li>
</ul>

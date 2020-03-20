<div class="container content-wrapper">

  
<p>Hi! 👋</p>


<p>If you haven't attempted to solve add yet, close this email and go do that now before reading on.
     If you have attempted solving add, read on...
</p>

<p>This function has to make a new list and that new list has to have more new
lists inside it. And we're going to need to loop over our old lists of lists
while doing that.</p>
<p>One of the trickier parts of this problem is the fact that you'll need to loop
over two lists at the same time.</p>
<p>You might think to do this with indexes:</p>
<pre><code>def add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices."""
    combined = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        combined.append(row)
    return combined
</code></pre>

<p>If you read my article on <a href="http://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/">looping with indexes in
Python</a>
you'll see that this isn't the best way to loop over two lists in Python (in
fact it isn't even the best way to loop with indexes in general).</p>
<p>Python's <code>zip</code> function can be handy for looping over two lists at the same
time.</p>
<pre><code>def add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices."""
    combined = []
    for rows in zip(matrix1, matrix2):
        row = []
        for items in zip(rows[0], rows[1]):
            row.append(items[0] + items[1])
        combined.append(row)
    return combined
</code></pre>

<p>Notice we're using <code>zip</code> twice because we need to loop over two lists at once
for both the outer lists and the inner lists.</p>
<p>Note that we have hard-coded indexes here. We can make our code more readable
by <a href="http://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/">embracing multiple assignment in Python</a> instead of hard-coding indexes.</p>
<pre><code>def add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices."""
    combined = []
    for row1, row2 in zip(matrix1, matrix2):
        row = []
        for n, m in zip(row1, row2):
            row.append(n + m)
        combined.append(row)
    return combined
</code></pre>

<p>If you've been doing Python for a little while you might spot a bit of code
that we could rewrite here. We're making an new empty list, looping over an
old list, and appending to the new list each time we loop like this:</p>
<pre><code>row = []
for n, m in zip(row1, row2):
    row.append(n + m)
</code></pre>

<p>Whenever you see code written like this, you could copy-paste this into a list
comprehension. Like this:</p>
<pre><code>new_row = [n+m for n, m in zip(row1, row2)]
</code></pre>

<p>Or even:</p>
<pre><code>row = [
    n + m
    for n, m in zip(row1, row2)
]
</code></pre>

<p>So we could copy-paste our list-building into a comprehension like this:</p>
<pre><code>def add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices."""
    combined = []
    for row1, row2 in zip(matrix1, matrix2):
        row = [
            n + m
            for n, m in zip(row1, row2)
        ]
        combined.append(row)
    return combined
</code></pre>

<p>Or we could remove that unnecessary variable like this:</p>
<pre><code>def add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices."""
    combined = []
    for row1, row2 in zip(matrix1, matrix2):
        combined.append([
            n + m
            for n, m in zip(row1, row2)
        ])
    return combined
</code></pre>

<p>If you're curious about how to copy-paste from a for loop to a comprehension
read <a href="http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/">my article on list comprehensions</a>.</p>
<p>I like to start by writing my comprehensions on one line of code. This one
might be short enough to be readable on one line though:</p>
<pre><code>def add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices."""
    combined = []
    for row1, row2 in zip(matrix1, matrix2):
        combined.append([n + m for n, m in zip(row1, row2)])
    return combined
</code></pre>

<p>You might notice that again we have something that we could copy-paste into a
comprehension (we're making an empty combined list and then appending while
looping).</p>
<p>We can copy-paste this loop into another comprehension:</p>
<pre><code>def add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices."""
    return [
        [n + m for n, m in zip(row1, row2)]
        for row1, row2 in zip(matrix1, matrix2)
    ]
</code></pre>

<p>We could write this on one line:</p>
<pre><code>def add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices."""
    return [[n+m for n, m in zip(r1, r2)] for r1, r2 in zip(matrix1, matrix2)]
</code></pre>

<p>But this definitely isn't easier than splitting this over multiple lines, so I
prefer the multi-line solution.</p>
<h1>Bonus #1</h1>
<p>Okay let's try to solve the first bonus.</p>
<p>For the first bonus we need to accept any number of matrices.</p>
<p>To do this we'll need to accept any number of arguments to our function and
pass any number of arguments to the <code>zip</code> function.  We can use <a href="https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/">the <code>*</code> operator</a>
for this.</p>
<pre><code>def add(*matrices):
    """Add corresponding numbers in given 2-D matrices."""
    combined = []
    for rows in zip(*matrices):
        row = []
        for values in zip(*rows):
            total = 0
            for n in values:
                total += n
            row.append(total)
        combined.append(row)
    return combined
</code></pre>

<p>Note that we've gone back to a for loops approach here.  We're no longer just
appending in our inner loop because we need to find a summation first.</p>
<p>We can use Python's sum function to sum up our values though:</p>
<pre><code>def add(*matrices):
    """Add corresponding numbers in given 2-D matrices."""
    combined = []
    for rows in zip(*matrices):
        row = []
        for values in zip(*rows):
            row.append(sum(values))
        combined.append(row)
    return combined
</code></pre>

<p>You might notice that this code has the same structure as our original nested
loops.  We could copy-paste this into two nested comprehensions again:</p>
<pre><code>def add(*matrices):
    """Add corresponding numbers in given 2-D matrices."""
    return [
        [sum(values) for values in zip(*rows)]
        for rows in zip(*matrices)
    ]
</code></pre>

<p>Notice that the existence of the <code>sum</code> function and the fact that the <code>zip</code>
function accepts any number of arguments were particularly helpful here.  We
couldn't have written this code as comprehensions without these essential
helper functions.</p>
<h1>Bonus #2</h1>
<p>For the second bonus, we were supposed to raise a ValueError exception when
our lists-of-lists were different shapes.</p>
<p>The answers for this one are somewhat complex.</p>
<p>If we ignored our first bonus, we could do this:</p>
<pre><code>def add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices."""
    if [len(r) for r in matrix1] != [len(r) for r in matrix2]:
        raise ValueError("Given matrices are not the same size.")
    return [
        [n + m for n, m in zip(row1, row2)]
        for row1, row2 in zip(matrix1, matrix2)
    ]
</code></pre>

<p>Notice that this works because you can deeply compare lists in Python.  We're
calculating the length of each of the inner lists and asserting that the outer
lists have the same length and that the inner lists all have the same
length... all in a single if statement!</p>
<p>If we wanted to do this with any number of matrices, we'd need to somehow
check for equality on many different lists.</p>
<p>If we use tuples instead of lists, we could use a set for this:</p>
<pre><code>def add(*matrices):
    """Add corresponding numbers in given 2-D matrices."""
    matrix_shapes = {
        tuple(len(r) for r in matrix)
        for matrix in matrices
    }
    if len(matrix_shapes) &gt; 1:
        raise ValueError("Given matrices are not the same size.")
    return [
        [sum(values) for values in zip(*rows)]
        for rows in zip(*matrices)
    ]
</code></pre>

<p>This might seem a little complex. We're using a set here because set items are
unique so if we pass in objects that are equal, we should only end up with 1
item in our set.</p>
<p>We can't pass in a list because lists aren't "hashable" because they're
mutable (they can be changed).  Tuples can be hashable so we're passing a
generator expression into the tuple constructor inside a set comprehension to
make a set of tuples.</p>
<p>Here's another answer:</p>
<pre><code>from itertools import zip_longest

def add(*matrices):
    """Add corresponding numbers in given 2-D matrices."""
    try:
        return [
            [sum(values) for values in zip_longest(*rows)]
            for rows in zip_longest(*matrices)
        ]
    except TypeError as e:
        raise ValueError("Given matrices are not the same size.") from e
</code></pre>

<p>This one is somewhat clever and may not be the clearest answer.</p>
<p>Python's built-in <code>zip</code> function stops at the shortest list when zipping.</p>
<p>The <code>zip_longest</code> function in the <code>itertools</code> module uses a fill value to return
missing items so the resulting list is as long as the longest gives list.</p>
<p>The default fill value for <code>zip_longest</code> is <code>None</code>, so looping over <code>None</code> would
fail and adding None to a number would fail too.  In both cases we'd get a
<code>TypeError</code> which is why we're catching a <code>TypeError</code> to handle the case where
matrices aren't the same size.</p>
<p>That <code>raise X from Y</code> syntax we're using is a Python 3 feature to make
tracebacks more clear.</p>
<p>Let's take a look at one more answer:</p>
<pre><code>def get_shape(matrix):
    return [len(r) for r in matrix]

def add(*matrices):
    """Add corresponding numbers in given 2-D matrices."""
    shape_of_matrix = get_shape(matrices[0])
    if any(get_shape(m) != shape_of_matrix for m in matrices):
        raise ValueError("Given matrices are not the same size.")
    return [
        [sum(values) for values in zip(*rows)]
        for rows in zip(*matrices)
    ]
</code></pre>

<p>Here we're using a <code>get_shape</code> function to get our list of list lengths for each
list and we're checking whether the shapes of each matrix is the same as the
shape of the first one (<code>matrices[0]</code>).</p>
<p>This is my favorite of the answers to the second bonus, but I don't find any
of them considerably more clear or succinct than the others.</p>
<p>I hope you learned something from these solutions. 😄</p>

</div>

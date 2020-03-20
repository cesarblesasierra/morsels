<div class="container content-wrapper">

      




    
      


<p>Hey! 👋</p>





<p>If you haven't attempted to solve fix_csv.py yet, close this email and go do that now before reading on.
     If you have attempted solving fix_csv.py, read on...
</p>

<p>This <code>fix_csv.py</code> program is supposed to accept the name of an existing pipe-delimited file and the name of a new comma-delimited file.</p>
<p>Here's one solution:</p>
<pre><code>import sys


old_filename = sys.argv[1]
new_filename = sys.argv[2]

old_file = open(old_filename)
rows = [
    line.split('|')
    for line in old_file.read().splitlines()
]

new_file = open(new_filename, mode='wt', newline='\r\n')
print("\n".join(
    ",".join(row)
    for row in rows
), file=new_file)
old_file.close()
new_file.close()
</code></pre>

<p>This solution doesn't pass our tests though.  One reason is that it doesn't
handle quotes when delimiters are in the output data.  We could use the csv
module to fix that.</p>
<pre><code>import csv
import sys


old_filename = sys.argv[1]
new_filename = sys.argv[2]

with open(old_filename, newline='') as old_file:
    reader = csv.reader(old_file, delimiter='|')
    rows = [line for line in reader]

with open(new_filename, mode='wt', newline='') as new_file:
    writer = csv.writer(new_file)
    writer.writerows(rows)
</code></pre>

<p>Notice that we've changed a couple different things here.</p>
<p>One big change is that we're using csv.reader and csv.writer to handle parsing
our delimited data files for us.  Notice that the csv module works for any
delimited data files, not just comma-delimited files.</p>
<p>Another change is that we're using "with" blocks here to ensure our files are
always automatically closed when we're done with them.</p>
<p>This still doesn't pass our tests though.  The reason is that our script
currently accepts more than 2 arguments and simply ignores all arguments after
the first two:</p>
<pre><code>$ python fix_csv.py in_file.psv out_file.csv another_arg and_another
</code></pre>

<p>We can fix this by slicing our arguments and unpacking them into exactly two
variables.</p>
<p>Instead of this:</p>
<pre><code>old_filename = sys.argv[1]
new_filename = sys.argv[2]
</code></pre>

<p>We'll do this:</p>
<pre><code>old_filename, new_filename = sys.argv[1:]
</code></pre>

<p>This is a lazy way of ensuring an exception is raised (even though it's not a
very friendly one) unless exactly 2 arguments are given (we're using <a href="http://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/">multiple assignment</a> here).</p>
<p>We could also improve this line:</p>
<pre><code>    rows = [line for line in reader]
</code></pre>

<p>Whenever you see a <a href="http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/">list comprehension</a> that loops over something and doesn't
filter anything or change any item but just makes a list, you can replace it
with the list constructor:</p>
<pre><code>    rows = list(reader)
</code></pre>

<p>The list constructor loops over whatever you give it and makes a new list.</p>
<p>If we wanted to, we could collapse this code a bit by writing one line for
both the reader and the writer:</p>
<pre><code>import csv
import sys


old_filename, new_filename = sys.argv[1:]

with open(old_filename, newline='') as old_file:
    rows = list(csv.reader(old_file, delimiter='|'))

with open(new_filename, mode='wt', newline='') as new_file:
    csv.writer(new_file).writerows(rows)
</code></pre>

<p>Notice in both of these open calls we've been specifying newline as an empty
string.  The reason that the CSV module writes \r\n line endings to our file
automatically, but Python will automatically take all LF endings (\n) and
convert them to CRLF endings (\r\n) on Windows systems.  So when writing CSV
files in Python 3, using newline='' is recommended.  In Python 2, you'll want
to use mode 'wb' instead for similar reasons.</p>
<p>The newline='' in the reading open isn't necessary because the CSV module
handles either \r\n and \n as line endings, but I think it's nice to be
consistent when opening files that are meant to represent CRLF-ended delimited
data.</p>
<p>Another thing I'll note about the csv reader and writer objects is that the
writer's writerows method takes an iterable and the reader object  <em>is</em>  an
iterable. So if we nested our with statements, we could actually write
directly while reading:</p>
<pre><code>import csv
import sys


old_filename, new_filename = sys.argv[1:]

with open(old_filename, newline='') as old_file:
    reader = csv.reader(old_file, delimiter='|')
    with open(new_filename, mode='wt', newline='') as new_file:
        csv.writer(new_file).writerows(reader)
</code></pre>

<p>This has a big benefit but also a downside.</p>
<p>The big benefit is that this allows us to efficiently process very large
delimited files because we're processing our files line-by-line here. Every
line that is read immediately results in one line that is written (because
reader reads lazily line by line and writerows loops lazily over the iterable
it's given as it's writing).</p>
<p>The downside is that if we provided the same filename for both input and
output, we'd get some weird results because we'd be writing to a file as we
were reading it which is often a bad idea.</p>
<p>So I'm going continue doing things the copy-into-list-and-use-two-with-blocks
way that we did above. If you'd prefer to write as you read, you could do pass
reader directly into the writer's writerows method instead though.</p>
<p>One more improvement we could make before jumping into the first bonus is to
make the command-line functionality of our script a bit more robust.</p>
<p>We can use <a href="https://docs.python.org/3/howto/argparse.html">argparse</a> from the
standard library to do that:</p>
<pre><code>from argparse import ArgumentParser
import csv


parser = ArgumentParser()
parser.add_argument('old_filename')
parser.add_argument('new_filename')
args = parser.parse_args()

with open(args.old_filename, newline='') as old_file:
    rows = list(csv.reader(old_file, delimiter='|'))

with open(args.new_filename, mode='wt', newline='') as new_file:
    csv.writer(new_file).writerows(rows)
</code></pre>

<p>The argparse library makes our command-line script have a friendly interface
that requires the correct number of arguments, shows usage information when -h
or --help flags are given, and shows helpful error messages when incorrect
command-line arguments are provided.</p>
<p>Using argparse will also make the first bonus easier.</p>
<p>Before we get to the first bonus, note that there are two other command-line
parsing tools in the standard library that you may hear about, but both are
focused on  <em>option</em>  parsing (for flags like -i and --in-quote) and neither
handles positional arguments from the command-line. See the section <a href="https://www.python.org/dev/peps/pep-0389/#why-aren-t-getopt-and-optparse-enough">why aren't getopt and optparse enough</a> from PEP 389 (the PEP that created argparse years ago).</p>
<h1>Bonus #1</h1>
<p>For this bonus we had to accept optional arguments for the delimiter and quote
character of the input data file.</p>
<p>We can modify our program to accept those arguments like this:</p>
<pre><code>from argparse import ArgumentParser
import csv


parser = ArgumentParser()
parser.add_argument('old_filename')
parser.add_argument('new_filename')
parser.add_argument('--in-delimiter', dest='delim')
parser.add_argument('--in-quote', dest='quote')
args = parser.parse_args()

with open(args.old_filename, newline='') as old_file:
    quotechar = '"'
    delimiter = '|'
    if args.delim:
        delimiter = args.delim
    if args.quote:
        quotechar = args.quote
    reader = csv.reader(old_file, delimiter=delimiter, quotechar=quotechar)
    rows = list(reader)

with open(args.new_filename, mode='wt', newline='') as new_file:
    writer = csv.writer(new_file)
    writer.writerows(rows)
</code></pre>

<p>We've added two more arguments to our argument parser and both are optional
(the default for arguments specified with --).</p>
<p>Note that we've added quite a bit of code to handle these new arguments when
reading our input file.  The default values for these arguments (if they're
unspecified) is None.  So we're defaulting them to | and " and only changing
those default values if they're "truthy" (None is falsey so evaluates to False
in that if condition).  You can think of truthiness as non-emptiness.</p>
<p>To make things easier we can set the default values for these arguments when
we add the arguments:</p>
<pre><code>from argparse import ArgumentParser
import csv


parser = ArgumentParser()
parser.add_argument('old_filename')
parser.add_argument('new_filename')
parser.add_argument('--in-delimiter', dest='delim', default='|')
parser.add_argument('--in-quote', dest='quote', default='"')
args = parser.parse_args()

with open(args.old_filename, newline='') as old_file:
    reader = csv.reader(old_file, delimiter=args.delim, quotechar=args.quote)
    rows = list(reader)

with open(args.new_filename, mode='wt', newline='') as new_file:
    writer = csv.writer(new_file)
    writer.writerows(rows)
</code></pre>

<p>This removes all the conditional checking and exceptional cases from our code.</p>
<p>Okay let's try the second bonus.</p>
<h1>Bonus #2</h1>
<p>This bonus was a bit tricky.  The objective was to automatically detect (or
attempt to detect) the format of the input file.</p>
<p>To do this, we can use the csv module's Sniffer class:</p>
<pre><code>from argparse import ArgumentParser
import csv


parser = ArgumentParser()
parser.add_argument('old_filename')
parser.add_argument('new_filename')
parser.add_argument('--in-delimiter', dest='delim')
parser.add_argument('--in-quote', dest='quote')
args = parser.parse_args()

with open(args.old_filename, newline='') as old_file:
    arguments = {}
    if args.delim:
        arguments['delimiter'] = args.delim
    if args.quote:
        arguments['quotechar'] = args.quote
    if not args.delim and not args.quote:
        arguments['dialect'] = csv.Sniffer().sniff(old_file.read())
        old_file.seek(0)
    reader = csv.reader(old_file, **arguments)
    rows = list(reader)

with open(args.new_filename, mode='wt', newline='') as new_file:
    writer = csv.writer(new_file)
    writer.writerows(rows)
</code></pre>

<p>Our code here is a bit complex.  If a delimiter and/or quote character are
specified, we provide keyword arguments for those to our csv reader object.
If neither is specified, then we use the csv Sniffer object to detect them.</p>
<p>Note that we're sniffing our entire csv file and then seeking back to the
beginning of the file so that we can start reading it again.  Files are
iterators which means they're stateful: they keep track of where we are in
them as we loop over them.</p>
<p>If you're unfamiliar with that <code>**</code> syntax, you might want to read the <a href="http://treyhunner.com/2018/04/keyword-arguments-in-python/">article I've written on keyword arguments in Python</a>.</p>
<p>I hope you found this exercise to be good practice for creating command-line
programs and working with delimited data!</p>


<img src="https://python.matomo.cloud/piwik.php?idsite=1&amp;rec=1&amp;bots=1&amp;e_c=exercises&amp;e_a=solutionEmailOpened&amp;uid=sergiomarreromarrero%40gmail.com" style="border:0;" alt="">


 

</div>

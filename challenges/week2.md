<div class="container content-wrapper">



<p>Hiya! 👋</p>
<p>This week we're going to normalize CSV files by writing a program, <code>fix_csv.py</code>, that turns a pipe-delimited file into a comma-delimited file.
I'll explain how it should work by example.</p>
<p>Your original file will look like this:</p>
<pre><code>Reading|Make|Model|Type|Value
Reading 0|Toyota|Previa|distance|19.83942
Reading 1|Dodge|Intrepid|distance|31.28257
</code></pre>
<p>You'll then run your script by typing this at the command line:</p>
<pre><code class="bash">$ python fix_csv.py cars-original.csv cars.csv
</code></pre>
<p><strong>Note</strong> : "$" is not typed; that is simply the beginning of the prompt.</p>
<p>Your fixed file should then look like this:</p>
<pre><code>Reading,Make,Model,Type,Value
Reading 0,Toyota,Previa,distance,19.83942
Reading 1,Dodge,Intrepid,distance,31.28257
</code></pre>
<p>Note that it's valid for a comma to be in your input data, but you'll need to surround data cells with commas in them by double quotes when writing your output file.</p>
<p>It's also valid for a quote character to be in your input (you'll need to double up quotes because <a href="https://stackoverflow.com/questions/17808511/properly-escape-a-double-quote-in-csv">that's how CSV escaping works</a>.</p>
<p>See the hints if you need help working with CSV files in Python.</p>
<p><strong>Bonus 1</strong></p>
<p>For the first bonus, I want you to allow the input delimiter and quote character (<code>"</code> by default) to be optionally specified. ✔️</p>
<p>For example any of these should work (all specify input delimiter as pipe and the last two additionally specifies the quote character as single quote):</p>
<pre><code class="bash">$ python fix_csv.py --in-delimiter="|" cars.csv cars-fixed.csv
$ python fix_csv.py cars.csv cars-fixed.csv --in-delimiter="|"
$ python fix_csv.py --in-delimiter="|" --in-quote="'" cars.csv cars-fixed.csv
$ python fix_csv.py --in-quote="|" --in-delimiter="," cars.csv cars-fixed.csv
</code></pre>
<p>This bonus will require looking into parsing command-line arguments with Python.
There are some standard library modules that can help you out with this.
There are 3 different solutions in the standard library actually, but only one I'd recommend.</p>
<p>Also note that if you're going to need Python to parse your CSV files for this bonus (or else you'll re-implement quite a bit of CSV-parsing code that's baked-in to Python).</p>
<p><strong>Bonus 2</strong></p>
<p>For the second bonus, try to automatically detect the delimiter if an in-delimiter value isn't supplied (don't assume it's pipe and quote, figure it out). ✔️</p>
<p>This second bonus is a bit trickier and I don't expect it to work correctly for all files.
Don't be afraid to check the hints for this one.</p>
<p><strong>Hints</strong></p>
<ul>
<li><a href="https://stackoverflow.com/a/35421024/2633215" title="You can see command-line arguments given to your program with sys.argv">How to access command-line arguments</a></li>
<li><a href="https://pymotw.com/3/csv/index.html" title="Doug Hellman explains Python's csv module">Reading and writing CSV files in Python</a></li>
<li><a href="https://www.youtube.com/watch?v=q5uM4VKywbA" title="This screencast discusses how CSV module is helpful in reading and writing a CSV file.">Short video on working with CSV files in Python</a></li>
<li><a href="https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/#Multiple_assignment_is_very_strict" title="Using tuple unpacking to validate the number of command-line arguments given">Restricting the number of command-line arguments</a></li>
<li><a href="http://zetcode.com/python/argparse/" title="An introduction to Python's argparse module">Parsing command-line arguments more robustly</a></li>
<li><a href="https://docs.python.org/3/library/csv.html#csv.Sniffer" title="The csv module has a Sniffer class for guessing the type of a CSV file">Automatically detecting the type of a CSV file</a></li>
</ul>


  </div>
</div>


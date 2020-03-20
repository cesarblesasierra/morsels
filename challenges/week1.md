<div id="body-wrapper">

   
<p>Hello! 😄</p>
<p>This week I want you to make a class that represents a circle.</p>
<p>The circle should have a <code>radius</code>, a <code>diameter</code>, and an <code>area</code>.
It should also have a nice string representation.</p>
<p>For example:</p>
<pre><code class="pycon">&gt;&gt;&gt; c = Circle(5)
&gt;&gt;&gt; c
Circle(5)
&gt;&gt;&gt; c.radius
5
&gt;&gt;&gt; c.diameter
10
&gt;&gt;&gt; c.area
78.53981633974483
</code></pre>
<p>Additionally the radius should default to 1 if no <code>radius</code> is specified when you
create your circle:</p>
<pre><code class="pycon">&gt;&gt;&gt; c = Circle()
&gt;&gt;&gt; c.radius
1
&gt;&gt;&gt; c.diameter
2
</code></pre>
<p>There are three bonuses for this exercise.</p>
<p><strong>Bonus 1</strong></p>
<p>For the first bonus, make sure when the <code>radius</code> of your class changes that the <code>diameter</code> and <code>area</code> both change as well: ✔️</p>
<pre><code class="pycon">&gt;&gt;&gt; c = Circle(2)
&gt;&gt;&gt; c.radius = 1
&gt;&gt;&gt; c.diameter
2
&gt;&gt;&gt; c.area
3.141592653589793
&gt;&gt;&gt; c
Circle(1)
</code></pre>
<p><strong>Bonus 2</strong></p>
<p>For the second bonus, make sure you can set the <code>diameter</code> attribute in your class and the <code>radius</code> will update accordingly.
Also make sure also that you cannot set the <code>area</code> (setting area should raise an <code>AttributeError</code>): ✔️</p>
<pre><code class="python">&gt;&gt;&gt; c = Circle(1)
&gt;&gt;&gt; c.diameter = 4
&gt;&gt;&gt; c.radius
2.0
&gt;&gt;&gt; c.area = 45.678
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "circle.py", line 16, in radius
AttributeError: can't set attribute
</code></pre>
<p><strong>Bonus 3</strong></p>
<p>For the third bonus, make sure your radius cannot be set to a negative number.
You should raise a <code>ValueError</code> exception with the error message "Radius cannot be negative".
✔️</p>
<pre><code class="pycon">&gt;&gt;&gt; c = Circle(5)
&gt;&gt;&gt; c.radius = 3
&gt;&gt;&gt; c.radius = -2
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "circle.py", line 27, in radius
    raise ValueError("Radius cannot be negative")
ValueError: Radius cannot be negative
</code></pre>
<p>This means that <code>diameter</code> cannot be negative either (and setting <code>diameter</code> to a negative number should also raise a <code>ValueError</code>).</p>
<p><strong>Hints</strong></p>
<p>Here are some hints you can use <strong>when you get stuck</strong> (hover over links to see what they're about):</p>
<ul>
<li><a href="https://www.youtube.com/watch?v=ZDa-Z5JzLYM/" title="How to make a class in Python">Creating a class</a></li>
<li><a href="https://www.youtube.com/watch?v=5cvM-crlDvg" title="You need to write a __repr__ method">String representation of a class</a></li>
<li><a href="https://docs.python.org/3/library/math.html#math.pi" title="You'll want to use pi from the math library">math things</a></li>
<li><a href="https://www.youtube.com/watch?v=jCzT9XFZ5bw" title="Properties are the way we make auto-updating attributes on Python classes">Making an auto-updating attribute</a></li>
<li><a href="https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python" title="Manually raising exceptions">Raising exceptions</a></li>
</ul>

    
   </div>

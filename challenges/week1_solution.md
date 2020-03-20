<div class="container content-wrapper">

     

<p>Hello!</p>





<p>If you haven't attempted to solve Circle yet, close this email and go do that now before reading on.
     If you have attempted solving Circle, read on...
</p>

<p>This week you needed to make a class that represents a circle. It should
including a radius, diameter, and area and the diameter and area should change
automatically based on the radius.</p>
<p>Let's start with an answer that doesn't quite work.</p>
<pre><code>import math

class Circle:
    """Circle with radius, area, and diameter."""
    def __init__(self, radius):
        self.radius = radius
        self.area = math.pi * self.radius ** 2
        self.diameter = self.radius * 2
</code></pre>

<p>Here we're setting all of our attributes in our initializer method, which gets
run each time a new instance of our class is created.</p>
<p>This answer is missing two features that we need: it doesn't default the
radius value to 1 (radius is required) and it doesn't have a useful string
representation.</p>
<p>The default string representation of our class looks something like this:</p>
<pre><code>&gt;&gt;&gt; c = Circle(1)
&gt;&gt;&gt; c
&lt;circle.Circle object at 0x7f75816c48d0&gt;
</code></pre>

<p>Which isn't very helpful for programmers who are using our class. We can fix
this by adding a <code>__repr__</code> method. We'll do that and then also add a default
value for the radius in our initializer method:</p>
<pre><code>import math

class Circle:

    """Circle with radius, area, and diameter."""

    def __init__(self, radius=1):
        self.radius = radius
        self.area = math.pi * self.radius ** 2
        self.diameter = self.radius * 2

    def __repr__(self):
        return f"Circle({self.radius})"

</code></pre>

<p>Here we're controlling the string representation of our class to return
something that looks like the code we'd execute to recreate an equivalent
class. Note that we're using an f-string for string formatting. This is an
alternative to using the format method or the % sign and this feature is only
available in Python 3.6+. Our string representation is much nicer now:</p>
<pre><code>&gt;&gt;&gt; c = Circle()
&gt;&gt;&gt; c
Circle(1)
</code></pre>

<p>Additionally we also don't need to specify a radius (it defaults to 1).</p>
<p>Also note that we don't need to implement <code>__str__</code>, the other string
representation. By default <code>__str__</code> relies on <code>__repr__</code>, so if they're the same
we only need to define <code>__repr__</code>.</p>
<p>This code passes all of our basic tests now.</p>
<p>Let's talk about the first bonus now.</p>
<h1>Bonus #1</h1>
<p>The first bonus required that when we change the radius, the diameter and area
change automatically.</p>
<p>To do this we need to make the diameter and area attributes into properties.
We can do that by using the property decorator:</p>
<pre><code>class Circle:

    """Circle with radius, area, and diameter."""

    def __init__(self, radius=1):
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.radius})"

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

</code></pre>

<p>With this new class, whenever the area and diameter attributes are accessed,
the corresponding methods will be executed and the returned value will be
provided as the value of the accessed attribute.</p>
<p><strong>If you've never seen properties before, you should definitely look them
up</strong>. They're Python's preferred equivalent to getter and setter methods
(which are popular in the Java world for example).</p>
<p>Let's attempt the second bonus now.</p>
<h1>Bonus #2</h1>
<p>The second bonus required that the diameter property be able to be set to a
value and that the radius would automatically change appropriately based on
the set value.</p>
<p>For this we need to make a setter for our diameter property. Here are just the
diameter property methods in our class:</p>
<pre><code>    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2
</code></pre>

<p>The syntax for property setters is a little weird. If you're unfamiliar with
that @ we've been using, that's the syntax for using a decorator in Python.
Python's built-in property class can be used as a decorator, but it can also
be used with a different syntax:</p>
<pre><code>    def get_diameter(self):
        return self.radius * 2

    def set_diameter(self, diameter):
        self.radius = diameter / 2

    diameter = property(get_diameter, set_diameter)

</code></pre>

<p>Personally I prefer the decorator syntax for properties so I use that @ syntax
pretty much exclusively. This one works fine too though.</p>
<p>We also needed to make sure that <code>area</code> wasn't settable.
The easiest way to do this was to not make a <code>setter</code> at all.
When you make a <code>property</code> without a setter method, attempting to set the property will raise an <code>AttributeError</code> automatically.</p>
<p>Now let's take a look at the final bonus now.</p>
<h1>Bonus #3</h1>
<p>For this bonus, we're supposed to make it so that the radius attribute cannot
be set to a negative number. This one might have required a bit more thought,
even if you've used properties before.</p>
<p>The key to this one was to realize that the radius attribute could also be
powered by a property:</p>
<pre><code>    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius &lt; 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius

</code></pre>

<p>Adding a getter and setter for the radius property is all we need to do to get
the bonus working. Whenever we set radius (like in our <code>__init__</code> method or our
diameter setter)  or access the radius (like in our diameter and area
getters), these getter and setter methods will be called.</p>
<p>You might think you need to update your <code>__init__</code> method to also assign to <code>self._radius</code> and handle that exceptional case.
But we don't!
The reason we don't is that by the time <code>__init__</code> is called, our class instance has been constructed and assigning to self.radius will call our radius setter automatically!
We're able to treat our <code>_radius</code> attribute as encapsulated in the property getter/setters.
We  <em>can</em>  change <code>_radius</code> outside, but there's not a good reason to do so.</p>
<p>Note that we were storing our actual <code>radius</code> in a <code>radius</code> attribute before, but we're using a <code>_radius</code> attribute now.
We're doing this for two reasons:</p>
<ol>
<li>We can't use a <code>radius</code> attribute to store this data because <code>my_circle.radius</code> will call our <code>radius</code> <code>property</code> and that will look up <code>self.radius</code> which looks up the same property infinitely so we'd get a recursion error.</li>
<li>That <code>_</code> is a convention in Python that means "this attribute is non-public by convention, so don't touch it unless you know what you're doing".
There's no such thing as private attributes in Python, but an underscore prefix is often used to declare an attribute as being an internal implementation detail, not to be touched by folks outside this class implementation.</li>
</ol>
<p>Here's a fully working solution that passes all the bonuses:</p>
<pre><code class="python">class Circle:

    """Circle with radius, area, and diameter."""

    def __init__(self, radius=1):
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.radius})"

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius &lt; 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius
</code></pre>

<p>Note that we didn't have to do anything special here to get <code>diameter</code> to not accept negative values.
That's because <code>diameter</code> sets <code>self.radius</code>, which calls our <code>radius</code> property setter.
Also note that we don't reference <code>self._radius</code> anywhere except in our <code>radius</code> property getter and setter methods: even <code>__init__</code> sets <code>self.radius</code> instead of <code>self._radius</code>.
We never touch that <code>self._radius</code> attribute directly but instead always go through our <code>radius</code> setter, so that every time that attribute is set it'll check for validity correctly.</p>
<p>Properties are really powerful in Python. Python's properties allow us to take
an existing attribute-based class API and maintain backwards compatibility
while adding new functionality during attribute lookup or assignment.</p>
<p>We now have a complete implementation of the Circle class which should pass
all of our tests.</p>
<p>I hope you learned something from this exercise about classes and properties
from these solutions. 😄</p>



    </div>

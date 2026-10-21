![](https://www.youtube.com/watch?v=fNk_zzaMoSs)

Beginning the linear algebra series with the basics.  
Help fund future projects: https://www.patreon.com/3blue1brown  
  
Music: https://vincerubinetti.bandcamp.com/track/grants-etude  
  
Thanks to Elo Marie Viennot and Ambros Gleixner from HTW Berlin (www.htw-berlin.de) for contributing German translations and dubbing.  
  
Thanks also to these viewers for their contributions to the subtitles  
Arabic: @Cewkins, Hazem  
Bengali: Md Rasheduzzaman  
Czech: @Chnapak  
Greek: Nikolaos Tsagkas  
Hebrew: Omer Tuchfeld  
Italian: mattiacolucci  
Spanish: Juan Carlos Largo  
Thai: own doggoV●ᴥ●V  
  
\------------------  
  
3blue1brown is a channel about animating math, in all senses of the word animate. And you know the drill with YouTube, if you want to stay posted about new videos, subscribe, and click the bell to receive notifications (if you're into that).  
  
If you are new to this channel and want to see more, a good place to start is this playlist: https://goo.gl/WmnCQZ  
  
Various social media stuffs:  
Website: https://www.3blue1brown.com  
Twitter: https://twitter.com/3Blue1Brown  
Patreon: https://patreon.com/3blue1brown  
Facebook: https://www.facebook.com/3blue1brown  
Reddit: https://www.reddit.com/r/3Blue1Brown

## Transcript

### Three perspectives on vectors

**0:00** · \[Translated by Grant Sanderson. Submit corrections at criblate.com\] The fundamental, root-of-it-all building block for linear algebra is the vector.

**0:15** · So it's worth making sure that we're all on the same page about what exactly a vector is.

**0:20** · You see, broadly speaking, there are three distinct but related ideas about vectors, which I'll call the physics student perspective, the computer science student perspective, and the mathematician's perspective.

**0:30** · The physics student perspective is that vectors are arrows pointing in space.

**0:34** · What defines a given vector is its length and the direction it's pointing, but as long as those two facts are the same, you can move it all around, and it's still the same vector.

**0:44** · Vectors that live in the flat plane are two-dimensional, and those sitting in broader space that you and I live in are three-dimensional.

**0:51** · The computer science perspective is that vectors are ordered lists of numbers.

**0:55** · For example, let's say you were doing some analytics about house prices, and the only features you cared about were square footage and price.

**1:03** · You might model each house with a pair of numbers, the first indicating square footage and the second indicating price.

**1:09** · Notice the order matters here.

**1:12** · In the lingo, you'd be modeling houses as two-dimensional vectors, where in this context, vector is pretty much just a fancy word for list, and what makes it two-dimensional is the fact that the length of that list is two.

**1:25** · The mathematician, on the other hand, seeks to generalize both these views, basically saying that a vector can be anything where there's a sensible notion of adding two vectors and multiplying a vector by a number, operations that I'll talk about later on in this video.

**1:39** · The details of this view are rather abstract, and I actually think it's healthy to ignore it until the last video of this series, favoring a more concrete setting in the interim.

**1:48** · But the reason I bring it up here is that it hints at the fact that the ideas of vector addition and multiplication by numbers will play an important role throughout linear algebra.

**1:58** · But before I talk about those operations, let's just settle in on a specific thought to have in mind when I say the word vector.

**2:04** · Given the geometric focus that I'm shooting for here, whenever I introduce a new topic involving vectors, I want you to first think about an arrow, and specifically, think about that arrow inside a coordinate system, like the xy-plane, with its tail sitting at the origin.

**2:19** · This is a little bit different from the physics student perspective, where vectors can freely sit anywhere they want in space.

**2:25** · In linear algebra, it's almost always the case that your vector will be rooted at the origin.

**2:30** · Then, once you understand a new concept in the context of arrows in space, we'll translate it over to the list of numbers point of view, which we can do by considering the coordinates of the vector.

**2:41** · Now, while I'm sure that many of you are already familiar with this coordinate system, it's worth walking through explicitly, since this is where all of the important back and forth happens between the two perspectives of linear algebra.

### Coordinates and space

**2:52** · Focusing our attention on two dimensions for the moment, you have a horizontal line, called the x-axis, and a vertical line, called the y-axis.

**3:00** · The place where they intersect is called the origin, which you should think of as the center of space and the root of all vectors.

**3:06** · After choosing an arbitrary length to represent one, you make tick marks on each axis to represent this distance.

**3:12** · When I want to convey the idea of 2D space as a whole, which you'll see comes up a lot in these videos, I'll extend these tick marks to make grid lines, but right now, they'll actually get a little bit in the way.

**3:22** · The coordinates of a vector is a pair of numbers that basically gives instructions for how to get from the tail of that vector at the origin to its tip.

**3:30** · The first number tells you how far to walk along the x-axis, positive numbers indicating rightward motion, negative numbers indicating leftward motion, and the second number tells you how far to walk parallel to the y-axis after that, positive numbers indicating upward motion, and negative numbers indicating downward motion.

**3:48** · To distinguish vectors from points, the convention is to write this pair of numbers vertically with square brackets around them.

**3:56** · Every pair of numbers gives you one and only one vector, and every vector is associated with one and only one pair of numbers.

**4:04** · What about in three dimensions?

**4:06** · Well, you add a third axis, called the z-axis, which is perpendicular to both the x and y-axes, and in this case, each vector is associated with ordered triplet of numbers.

**4:16** · The first tells you how far to move along the x-axis, the second tells you how far to move parallel to the y-axis, and the third one tells you how far to then move parallel to this new z-axis.

**4:28** · Every triplet of numbers gives you one unique vector in space, and every vector in space gives you exactly one triplet of numbers.

**4:36** · All right, so back to vector addition and multiplication by numbers.

**4:40** · After all, every topic in linear algebra is going to center around these two operations.

### Vector addition

**4:45** · Luckily, each one's pretty straightforward to define.

**4:48** · Let's say we have two vectors, one pointing up and a little to the right, and the other one pointing right and down a bit.

**4:53** · To add these two vectors, move the second one so that its tail sits at the tip of the first one.

**5:00** · Then, if you draw a new vector from the tail of the first one to where the tip of the second one sits, that new vector is their sum.

**5:12** · This definition of addition, by the way, is pretty much the only time in linear algebra where we let vectors stray away from the origin.

**5:19** · Now, why is this a reasonable thing to do?

**5:21** · Why this definition of addition and not some other one?

**5:25** · Well, the way I like to think about it is that each vector represents a certain movement, a step with a certain distance and direction in space.

**5:33** · If you take a step along the first vector, then take a step in the direction and distance described by the second vector, the overall effect is just the same as if you moved along the sum of those two vectors to start with.

**5:45** · You could think about this as an extension of how we think about adding numbers on a number line.

**5:50** · One way that we teach kids to think about this, say with 2 plus 5, is to think of moving two steps to the right followed by another five steps to the right.

**5:57** · The overall effect is the same as if you just took seven steps to the right.

**6:02** · In fact, let's see how vector addition looks numerically.

**6:06** · The first vector here has coordinates 1, 2, and the second one has coordinates 3, negative 1.

**6:14** · When you take the vector sum using this tip-to-tail method, you can think of a four-step path from the origin to the tip of the second vector.

**6:21** · Walk 1 to the right, then 2 up, then 3 to the right, then 1 down.

**6:26** · Reorganizing these steps so that you first do all of the rightward motion, then do all the vertical motion, you can read it as saying first move 1 plus 3 to the right, then move 2 minus 1 up.

**6:40** · So the new vector has coordinates 1 plus 3 and 2 plus negative 1.

**6:45** · In general, vector addition in this list of numbers conception looks like matching up their terms and adding each one together.

### Scalar multiplication

**6:54** · The other fundamental vector operation is multiplication by a number.

**6:58** · Now this is best understood just by looking at a few examples.

**7:01** · If you take the number 2 and multiply it by a given vector, it means you stretch out that vector so that it's two times as long as when you started.

**7:10** · If you multiply that vector by, say, one-third, it means you squish it down so that it's one-third the original length.

**7:17** · When you multiply it by a negative number, like negative 1.8, then the vector first gets flipped around, then stretched out by that factor of 1.8.

**7:27** · This process of stretching or squishing or sometimes reversing the direction of a vector is called scaling, and whenever you catch a number like two or one-third or negative 1.8 acting like this, scaling some vector, you call it a scalar.

**7:41** · In fact, throughout linear algebra, one of the main things that numbers do is scale vectors, so it's common to use the word scalar pretty much interchangeably with the word number.

**7:52** · Numerically, stretching out a vector by a factor of, say, 2, corresponds with multiplying each of its components by that factor, 2.

**8:00** · So in the conception of vectors as lists of numbers, multiplying a given vector by a scalar means multiplying each one of those components by that scalar.

**8:10** · You'll see in the following videos what I mean when I say linear algebra topics tend to revolve around these two fundamental operations, vector addition and scalar multiplication.

### Connecting the perspectives

**8:19** · And I'll talk more in the last video about how and why the mathematician thinks only about these operations, independent and abstracted away from however you choose to represent vectors.

**8:29** · In truth, it doesn't matter whether you think about vectors as fundamentally being arrows in space, like I'm suggesting you do, that happen to have a nice numerical representation, or fundamentally as lists of numbers that happen to have a nice geometric interpretation.

**8:42** · The usefulness of linear algebra has less to do with either one of these views than it does with the ability to translate back and forth between them.

**8:50** · It gives the data analyst a nice way to conceptualize many lists of numbers in a visual way, which can seriously clarify patterns in data and give a global view of what certain operations do.

**9:00** · And on the flip side, it gives people like physicists and computer graphics programmers a language to describe space and the manipulation of space using numbers that can be crunched and run through a computer.

**9:12** · When I do math-y animations, for example, I start by thinking about what's actually going on in space, and then get the computer to represent things numerically, thereby figuring out where to place the pixels on the screen.

**9:23** · And doing that usually relies on a lot of linear algebra understanding.

**9:27** · So there are your vector basics, and in the next video I'll start getting into some pretty neat concepts surrounding vectors like span, bases, and linear dependence.

**9:49** · See you then!
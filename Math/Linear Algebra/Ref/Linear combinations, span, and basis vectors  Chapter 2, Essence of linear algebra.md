![](https://www.youtube.com/watch?v=k7RM-ot2NWY)

The fundamental concepts of span, linear combinations, linear dependence, and bases.  
Help fund future projects: https://www.patreon.com/3blue1brown  
  
Thanks to Elo Marie Viennot and Ambros Gleixner from HTW Berlin (www.htw-berlin.de) for contributing German translations and dubbing.  
  
Thanks to these viewers for their contributions to translations  
Arabic: @Cewkins, Hazem  
Hebrew: Omer Tuchfeld  
Spanish: Juan Carlos Largo  
Vietnamese: @ngvutuan2811  
  
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

### Basis vectors and scalars

**0:11** · In the last video, along with the ideas of vector addition and scalar multiplication, I described vector coordinates, where there's this back and forth between, for example, pairs of numbers and two-dimensional vectors.

**0:23** · Now, I imagine the vector coordinates were already familiar to a lot of you, but there's another kind of interesting way to think about these coordinates, which is pretty central to linear algebra.

**0:32** · When you have a pair of numbers that's meant to describe a vector, like 3, negative 2, I want you to think about each coordinate as a scalar, meaning, think about how each one stretches or squishes vectors.

**0:45** · In the xy coordinate system, there are two very special vectors, the one pointing to the right with length 1, commonly called i-hat, or the unit vector in the x direction, and the one pointing straight up with length 1, commonly called j-hat, or the unit vector in the y direction.

**1:02** · Now, think of the x coordinate of our vector as a scalar that scales i-hat, stretching it by a factor of 3, and the y coordinate as a scalar that scales j-hat, flipping it and stretching it by a factor of 2.

**1:14** · In this sense, the vector that these coordinates describe is the sum of two scaled vectors.

**1:20** · That's a surprisingly important concept, this idea of adding together two scaled vectors.

**1:27** · Those two vectors, i-hat and j-hat, have a special name, by the way.

### Linear combinations

**1:30** · Together, they're called the basis of a coordinate system.

**1:34** · What this means, basically, is that when you think about coordinates as scalars, the basis vectors are what those scalars actually, you know, scale.

**1:42** · There's also a more technical definition, but I'll get to that later.

**1:47** · By framing our coordinate system in terms of these two special basis vectors, it raises a pretty interesting and subtle point.

**1:54** · We could have chosen different basis vectors and gotten a completely reasonable new coordinate system.

**2:01** · For example, take some vector pointing up and to the right, along with some other vector pointing down and to the right in some way.

**2:07** · Take a moment to think about all the different vectors that you can get by choosing two scalars, using each one to scale one of the vectors, then adding together what you get.

**2:17** · Which two-dimensional vectors can you reach by altering the choices of scalars?

**2:24** · The answer is that you can reach every possible two-dimensional vector, and I think it's a good puzzle to contemplate why.

**2:32** · A new pair of basis vectors like this still gives us a valid way to go back and forth between pairs of numbers and two-dimensional vectors, but the association is definitely different from the one that you get using the more standard basis of i-hat and j-hat.

**2:46** · This is something I'll go into much more detail on later, describing the exact relationship between different coordinate systems, but for right now, I just want you to appreciate the fact that any time we describe vectors numerically, it depends on an implicit choice of what basis vectors we're using.

**3:02** · So any time that you're scaling two vectors and adding them like this, it's called a linear combination of those two vectors.

### Understanding span

**3:11** · Where does this word linear come from?

**3:12** · Why does this have anything to do with lines?

**3:14** · Well, this isn't the etymology, but one way I like to think about it is that if you fix one of those scalars and let the other one change its value freely, the tip of the resulting vector draws a straight line.

**3:29** · Now, if you let both scalars range freely and consider every possible vector that you can get, there are two things that can happen.

**3:36** · For most pairs of vectors, you'll be able to reach every possible point in the plane.

**3:40** · Every two-dimensional vector is within your grasp.

**3:43** · However, in the unlucky case where your two original vectors happen to line up, the tip of the resulting vector is limited to just this single line passing through the origin.

**3:53** · Actually, technically there's a third possibility too.

**3:56** · Both your vectors could be zero, in which case you'd just be stuck at the origin.

**4:01** · Here's some more terminology.

**4:02** · The set of all possible vectors that you can reach with a linear combination of a given pair of vectors is called the span of those two vectors.

**4:14** · So restating what we just saw in this lingo, the span of most pairs of 2D vectors is all vectors of 2D space, but when they line up, their span is all vectors whose tip sit on a certain line.

**4:27** · Remember how I said that linear algebra revolves around vector addition and scalar multiplication?

**4:31** · Well, the span of two vectors is basically a way of asking what are all the possible vectors you can reach using only these two fundamental operations, vector addition and scalar multiplication.

### Vectors as points

**4:43** · This is a good time to talk about how people commonly think about vectors as points.

**4:47** · It gets really crowded to think about a whole collection of vectors sitting on a line, and more crowded still to think about all two-dimensional vectors all at once, filling up the plane.

**4:57** · So when dealing with collections of vectors like this, it's common to represent each one with just a point in space, the point at the tip of that vector where, as usual, I want you thinking about that vector with its tail on the origin.

**5:10** · That way, if you want to think about every possible vector whose tip sits on a certain line, just think about the line itself.

**5:19** · Likewise, to think about all possible two-dimensional vectors all at once, conceptualize each one as the point where its tip sits.

**5:27** · So in effect, what you'll be thinking about is the infinite flat sheet of two-dimensional space itself, leaving the arrows out of it.

**5:36** · In general, if you're thinking about a vector on its own, think of it as an arrow.

**5:40** · And if you're dealing with a collection of vectors, it's convenient to think of them all as points.

**5:45** · So for our span example, the span of most pairs of vectors ends up being the entire infinite sheet of two-dimensional space.

**5:52** · But if they line up, their span is just a line.

### Span in 3D

**5:58** · The idea of span gets a lot more interesting if we start thinking about vectors in three-dimensional space.

**6:04** · For example, if you take two vectors in 3D space that are not pointing in the same direction, what does it mean to take their span?

**6:13** · Well, their span is the collection of all possible linear combinations of those two vectors, meaning all possible vectors you get by scaling each of the two of them in some way and then adding them together.

**6:25** · You can kind of imagine turning two different knobs to change the two scalars defining the linear combination, adding the scaled vectors and following the tip of the resulting vector.

**6:36** · That tip will trace out some kind of flat sheet cutting through the origin of three-dimensional space.

**6:41** · This flat sheet is the span of the two vectors.

**6:45** · Or more precisely, the set of all possible vectors whose tips sit on that flat sheet is the span of your two vectors.

**6:51** · Isn't that a beautiful mental image?

**6:54** · So, what happens if we add a third vector and consider the span of all three of those guys?

**7:00** · A linear combination of three vectors is defined pretty much the same way as it is for two.

**7:05** · You'll choose three different scalars, scale each of those vectors, and then add them all together.

**7:15** · And again, the span of these vectors is the set of all possible linear combinations.

**7:24** · Two different things could happen here.

### Linear dependence

**7:26** · If your third vector happens to be sitting on the span of the first two, then the span doesn't change.

**7:31** · You're sort of trapped on that same flat sheet.

**7:34** · In other words, adding a scaled version of that third vector to the linear combination doesn't really give you access to any new vectors.

**7:42** · But if you just randomly choose a third vector, it's almost certainly not sitting on the span of those first two.

**7:48** · Then, since it's pointing in a separate direction, it unlocks access to every possible three-dimensional vector.

**7:55** · One way I like to think about this is that as you scale that new third vector, it moves around that span sheet of the first two, sweeping it through all of space.

**8:05** · Another way to think about it is that you're making full use of the three freely changing scalars that you have at your disposal to access the full three dimensions of space.

**8:16** · Now, in the case where the third vector was already sitting on the span of the first two, or the case where two vectors happen to line up, we want some terminology to describe the fact that at least one of these vectors is redundant, not adding anything to our span.

**8:30** · Whenever this happens, where you have multiple vectors and you could remove one without reducing the span, the relevant terminology is to say that they are linearly dependent.

**8:40** · Another way of phrasing that would be to say that one of the vectors can be expressed as a linear combination of the others, since it's already in the span of the others.

**8:52** · On the other hand, if each vector really does add another dimension to the span, they're said to be linearly independent.

**9:06** · So with all of that terminology, and hopefully with some good mental images to go with it, let me leave you with a puzzle before we go.

### Basis definition quiz

**9:12** · The technical definition of a basis of a space is a set of linearly independent vectors that span that space.

**9:22** · Now, given how I described a basis earlier, and given your current understanding of the words span and linearly independent, think about why this definition would make sense.

**9:33** · In the next video, I'll get into matrices in transforming space. See you then!
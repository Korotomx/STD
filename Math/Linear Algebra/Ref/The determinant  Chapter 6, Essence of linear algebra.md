![](https://www.youtube.com/watch?v=Ip3X9LOh2dk)

The determinant measures how much volumes change during a transformation.  
Help fund future projects: https://www.patreon.com/3blue1brown  
An equally valuable form of support is to simply share some of the videos.  
Home page: https://www.3blue1brown.com/  
  
  
Full series: http://3b1b.co/eola  
  
Future series like this are funded by the community, through Patreon, where supporters get early access as the series is being produced.  
http://3b1b.co/support  
  
Thanks to these viewers for their contributions to translations  
Hebrew: Omer Tuchfeld  
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

### Understanding determinants

**0:00** · \[Submit subtitle corrections at criblate.com\] Hello, hello again.

**0:13** · So moving forward, I'll be assuming that you have a visual understanding of linear transformations and how they're represented with matrices, the way that I've been talking about in the last few videos.

**0:22** · If you think about a couple of these linear transformations, you might notice how some of them seem to stretch space out, while others squish it on in.

**0:31** · One thing that turns out to be pretty useful for understanding one of these transformations is to measure exactly how much it stretches or squishes things.

**0:39** · More specifically, to measure the factor by which the area of a given region increases or decreases.

**0:47** · For example, look at the matrix with columns (3, 0) and (0, 2).

**0:51** · It scales i-hat by a factor of 3 and scales j-hat by a factor of 2.

**0:56** · Now, if we focus our attention on the 1 by 1 square whose bottom sits on i-hat and whose left side sits on j-hat, after the transformation, this turns into a 2 by 3 rectangle.

**1:08** · Since this region started out with area 1 and ended up with area 6, we can say the linear transformation has scaled its area by a factor of 6.

**1:18** · Compare that to a shear, whose matrix has columns (1, 0) and (1, 1), meaning i-hat stays in place and j-hat moves over to (1, 1).

**1:27** · That same unit square determined by i-hat and j-hat gets slanted and turned into a parallelogram, but the area of that parallelogram is still 1, since its base and height each continue to have length 1.

**1:39** · So even though this transformation smushes things about, it seems to leave areas unchanged, at least in the case of that 1 unit square.

**1:46** · Actually though, if you know how much the area of that one single unit square changes, it can tell you how the area of any possible region in space changes.

**1:56** · For starters, notice that whatever happens to one square in the grid has to happen to any other square in the grid, no matter the size.

**2:04** · This follows from the fact that grid lines remain parallel and evenly spaced.

**2:08** · Then, any shape that's not a grid square can be approximated by grid squares pretty well, with arbitrarily good approximations if you use small enough grid squares.

**2:17** · So, since the areas of all those tiny grid squares are being scaled by some single amount, the area of the blob as a whole will also be scaled by that same single amount.

**2:28** · This very special scaling factor, the factor by which a linear transformation changes any area, is called the determinant of that transformation.

### Interpreting 2D determinants

**2:39** · I'll show how to compute the determinant of a transformation using its matrix later on in this video, but understanding what it represents is, trust me, much more important than the computation.

**2:49** · For example, the determinant of a transformation would be 3 if that transformation increases the area of a region by a factor of 3. 41 00:02:58,180 --> 00:02:57,622 The determinant of a transformation would be ½ 42 00:02:57,622 --> 00:02:57,040 if it squishes down all areas by a factor of ½.

**2:58** · The determinant of a transformation would be 1 half if it squishes down all areas by a factor of 1 half. And the determinant of a 2D transformation is 0 if it squishes all of space onto a line, or even onto a single point.

**3:14** · Since then, the area of any region would become zero.

**3:17** · That last example will prove to be pretty important.

**3:20** · It means that checking if the determinant of a given matrix is zero will give a way of computing whether or not the transformation associated with that matrix squishes everything into a smaller dimension.

**3:30** · You'll see in the next few videos why this is even a useful thing to think about, but for now, I just want to lay down all of the visual intuition, which, in and of itself, is a beautiful thing to think about.

### Negative determinants

**3:42** · Okay, I need to confess that what I've said so far is not quite right.

**3:45** · The full concept of the determinant allows for negative values.

**3:49** · But what would the idea of scaling an area by a negative amount even mean?

**3:54** · This has to do with the idea of orientation.

**3:57** · For example, notice how this transformation gives the sensation of flipping space over.

**4:03** · If you were thinking of 2D space as a sheet of paper, a transformation like that one seems to turn over that sheet onto the other side.

**4:10** · Any transformations that do this are said to invert the orientation of space.

**4:15** · Another way to think about it is in terms of i-hat and j-hat.

**4:19** · Notice that in their starting positions, j-hat is to the left of i-hat.

**4:23** · If, after a transformation, j-hat is now on the right of i-hat, the orientation of space has been inverted.

**4:32** · Whenever this happens, whenever the orientation of space is inverted, the determinant will be negative.

**4:37** · The absolute value of the determinant, though, still tells you the factor by which areas have been scaled.

**4:43** · For example, the matrix with columns (1, 1) and (2, -1) encodes a transformation that has determinant, I'll just tell you, negative 3.

**4:51** · And what this means is that space gets flipped over and areas are scaled by a factor of 3.

**4:57** · So why would this idea of a negative area scaling factor be a natural way to describe orientation flipping?

**5:04** · Think about the series of transformations you get by slowly letting i-hat get closer and closer to j-hat.

**5:10** · As i-hat gets closer, all of the areas in space are getting squished more and more, meaning the determinant approaches 0.

**5:17** · Once i-hat lines up perfectly with j-hat, the determinant is 0.

**5:22** · Then, if i-hat continues the way that it was going, doesn't it kind of feel natural for the determinant to keep decreasing into the negative numbers?

**5:30** · So that's the understanding of determinants in two dimensions.

### Determinants in 3D

**5:33** · What do you think it should mean for three dimensions?

**5:36** · It also tells you how much a transformation scales things, but this time, it tells you how much volumes get scaled.

**5:45** · Just as in two dimensions, where this is easiest to think about by focusing on one particular square with an area 1 and watching only what happens to it, in three dimensions, it helps to focus your attention on the specific 1 by 1 by 1 cube whose edges are resting on the basis vectors, i-hat, j-hat and k-hat.

**6:04** · After the transformation, that cube might get warped into some kind of slanty slanty cube.

**6:10** · This shape, by the way, has the best name ever, parallelipiped, a name that's made even more delightful when your professor has a nice thick Russian accent.

**6:18** · Since this cube starts out with a volume of 1, and the determinant gives the factor by which any volume is scaled, you can think of the determinant simply as being the volume of that parallelipiped that the cube turns into.

**6:32** · A determinant of 0 would mean that all of space is squished onto something with 0 volume, meaning either a flat plane, a line, or, in the most extreme case, onto a single point.

**6:43** · Those of you who watched chapter 2 will recognize this as meaning that the columns of the matrix are linearly dependent.

**6:49** · Can you see why?

**6:54** · What about negative determinants?

**6:56** · What should that mean for three dimensions?

**6:58** · One way to describe orientation in 3D is with the right hand rule.

**7:03** · Point the forefinger of your right hand in the direction of i-hat, stick out your middle finger in the direction of j-hat, and notice how when you point your thumb up, it's in the direction of k-hat.

**7:14** · If you can still do that after the transformation, orientation has not changed, and the determinant is positive.

**7:21** · Otherwise, if after the transformation it only makes sense to do that with your left hand, orientation has been flipped, and the determinant is negative.

### Computing determinants

**7:31** · So, if you haven't seen it before, you're probably wondering by now, how do you actually compute the determinant?

**7:37** · For a 2x2 matrix with entries a, b, c, d, the formula is a times d minus b times c.

**7:45** · Here's part of an intuition for where this formula comes from.

**7:48** · Let's say that the terms b and c both happened to be 0.

**7:51** · Then, the term a tells you how much i-hat is stretched in the x direction, and the term d tells you how much j-hat is stretched in the y direction.

**8:02** · So, since those other terms are 0, it should make sense that a times d gives the area of the rectangle that our favorite unit square turns into, kind of like the 3, 0, 0, 2 example from earlier.

**8:15** · Even if only one of b or c are 0, you'll have a parallelogram with a base a and a height d.

**8:21** · So, the area should still be a times d.

**8:25** · Loosely speaking, if both b and c are non-zero, then that b times c term tells you how much this parallelogram is stretched or squished in the diagonal direction.

**8:36** · For those of you hungry for a more precise description of this b times c term, here's a helpful diagram if you'd like to pause and ponder.

**8:43** · Now, if you feel like computing determinants by hand is something that you need to know, the only way to get it down is to just practice it with a few.

**8:51** · There's really not that much I can say or animate that's going to drill in the computation.

**8:56** · This is all triply true for three-dimensional determinants.

**8:59** · There is a formula, and if you feel like that's something you need to know, you should practice with a few matrices, or, you know, go watch Sal Khan work through a few.

**9:07** · Honestly, though, I don't think that those computations fall within the essence of linear algebra, but I definitely think that understanding what the determinant represents falls within that essence.

### Closing thoughts

**9:18** · Here's kind of a fun question to think about before the next video.

**9:20** · If you multiply two matrices together, the determinant of the resulting matrix is the same as the product of the determinants of the original two matrices.

**9:31** · If you tried to justify this with numbers, it would take a really long time, but see if you can explain why this makes sense in just one sentence.

**9:42** · Next up, I'll be relating the idea of linear transformations covered so far to one of the areas where linear algebra is most useful, linear systems of equations. See you then!